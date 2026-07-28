// ==========================
// Analysis
// ==========================

document.addEventListener("DOMContentLoaded", () => {

    const btn = document.getElementById("startAnalysis");

    if (btn) {

        btn.addEventListener("click", startAnalysis);

    }

    const fixBtn = document.getElementById("autoFixBtn");

    if (fixBtn) {
        fixBtn.addEventListener("click", autoFixCode);
    }

});

async function startAnalysis() {

    const projectId = localStorage.getItem("project_id");

    if (!projectId) {

        alert("Please upload a project first.");

        return;

    }

    const progressBar = document.getElementById("progressBar");
    const progressText = document.getElementById("progressText");

    progressBar.style.width = "10%";
    progressText.innerText = "Starting Analysis...";

    try {

        const response = await fetch(

            `${API}/analysis/project/${projectId}`,

            {

                method: "POST"

            }

        );

        const data = await response.json();

        console.log("Analysis Response:", data);

        if (data.status !== "success") {

            alert("Analysis Failed");

            return;

        }

        const result = data.analysis;

        localStorage.setItem(
            "analysis",
            JSON.stringify(result)
        );

        progressBar.style.width = "100%";

        progressText.innerText = "Analysis Completed";

        updateDashboard(result);

    }

    catch(err){

        console.error(err);

        progressBar.style.width="0%";

        progressText.innerText="Analysis Failed";

        alert("Server Error");

    }

}



// ==========================
// Update Dashboard
// ==========================

function updateDashboard(result) {

    // ==========================
    // Cards
    // ==========================

    document.getElementById("qualityScore").innerText =
        result.project_score ?? "--";

    document.getElementById("securityScore").innerText =
        result.security_score ?? "--";

    document.getElementById("bugs").innerText =
        result.total_bugs ?? 0;

    if (typeof result.coverage === "object") {

        document.getElementById("coverage").innerText =
            (result.coverage.coverage_percent ?? 0) + "%";

    } else {

        document.getElementById("coverage").innerText =
            result.coverage ?? "--";

    }

    // ==========================
    // Report
    // ==========================

    document.getElementById("report").innerText =
        result.final_report || "No Report Available";

    document.getElementById("executiveSummary").innerText =
        result.executive_summary || "No Executive Summary";

    document.getElementById("projectStatus").innerText =
        result.overall_status || "--";

    // ==========================
    // Recommendations
    // ==========================

    const recommendationList =
        document.getElementById("recommendationList");

    recommendationList.innerHTML = "";

    if (result.recommendations &&
        result.recommendations.length > 0) {

        result.recommendations.forEach(item => {

            recommendationList.innerHTML +=
                `<li>${item}</li>`;

        });

    } else {

        recommendationList.innerHTML =
            "<li>No Recommendations</li>";

    }

    // ==========================
    // Tables
    // ==========================

    fillBugTable(result);

    fillSecurityTable(result);

    fillPerformanceTable(result);

    fillSmellTable(result);

    // ==========================
    // PDF
    // ==========================

    document.getElementById("downloadPdf").onclick = function () {

        const analysis = JSON.parse(localStorage.getItem("analysis"));

        if (!analysis || !analysis.pdf_report) {
            alert("PDF Report Not Found");
            return;
        }

        const fileName = analysis.pdf_report
            .replace(/\\/g, "/")
            .split("/")
            .pop();

        window.open(API + "/report_files/" + fileName, "_blank");
    };

    // ==========================
    // Charts
    // ==========================

    if (typeof loadCharts === "function") {

        loadCharts();

    }

    // ==========================
    // History
    // ==========================

    if (typeof loadHistory === "function") {

        loadHistory();

    }

    alert("Analysis Completed Successfully");

}


// ==========================
// BUG TABLE
// ==========================

function fillBugTable(result){

    const tbody=document.querySelector("#bugTable tbody");

    tbody.innerHTML="";

    const reports=result.file_reports || [];

    if(reports.length===0){

        tbody.innerHTML=`
        <tr>
            <td colspan="3" style="text-align:center">
                No Bugs Found
            </td>
        </tr>`;

        return;
    }

    reports.forEach((item,index)=>{

        tbody.innerHTML+=`
        <tr>

            <td>${item.file}</td>

            <td style="max-width:400px;white-space:pre-wrap;">
                ${JSON.stringify(item.bugs,null,2)}
            </td>

            <td>

                <button
                    class="btn btn-warning"
                    onclick="autoFix(${index})">

                    -------

                </button>

            </td>

        </tr>`;
    });

}

// ==========================
// SECURITY TABLE
// ==========================

function fillSecurityTable(result){

    const tbody=document.querySelector("#securityTable tbody");

    tbody.innerHTML="";

    const reports=result.file_reports || [];

    if(reports.length===0){

        tbody.innerHTML=`
        <tr>
            <td colspan="3" style="text-align:center">
                No Security Issues
            </td>
        </tr>`;

        return;
    }

    reports.forEach(item=>{

        tbody.innerHTML+=`
        <tr>
            <td>${item.file}</td>
            <td>${item.security || "Secure"}</td>
            <td>${item.security ? "High" : "Low"}</td>
        </tr>`;

    });

}

// ==========================
// PERFORMANCE TABLE
// ==========================

function fillPerformanceTable(result){

    const tbody=document.querySelector("#performanceTable tbody");

    tbody.innerHTML="";

    const reports=result.file_reports || [];

    if(reports.length===0){

        tbody.innerHTML=`
        <tr>
            <td colspan="2" style="text-align:center">
                No Performance Issues
            </td>
        </tr>`;

        return;
    }

    reports.forEach(item=>{

        tbody.innerHTML+=`
        <tr>
            <td>${item.file}</td>
            <td>${item.performance || "Good"}</td>
        </tr>`;

    });

}

// ==========================
// CODE SMELLS TABLE
// ==========================

function fillSmellTable(result){

    const tbody=document.querySelector("#smellTable tbody");

    tbody.innerHTML="";

    const reports=result.file_reports || [];

    if(reports.length===0){

        tbody.innerHTML=`
        <tr>
            <td colspan="2" style="text-align:center">
                Clean Code
            </td>
        </tr>`;

        return;
    }

    reports.forEach(item=>{

        tbody.innerHTML+=`
        <tr>
            <td>${item.file}</td>
            <td>${item.code_smells || "Clean Code"}</td>
        </tr>`;

    });

}



// NEW----->>

async function autoFix(index){

    const analysis=JSON.parse(localStorage.getItem("analysis"));

    const file=analysis.file_reports[index];

    const response=await fetch(`${API}/bugfix`,{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            code:file.code

        })

    });

    const data=await response.json();

    if(data.status!="success"){

        alert("Fix Failed");

        return;

    }

    const fixed=data.fixed_code;

    const w=window.open("","_blank");

    w.document.write(`

    <h2>${file.file}</h2>

    <h3>Original Code</h3>

    <pre>${file.code}</pre>

    <hr>

    <h3>Fixed Code</h3>

    <pre>${fixed}</pre>

    <button onclick="
    navigator.clipboard.writeText(document.querySelectorAll('pre')[1].innerText)
    ">
    Copy
    </button>

    `);

}



// new 

async function autoFixCode() {

    const projectPath = localStorage.getItem("project_path");

    if (!projectPath) {

        alert("Upload project first.");

        return;

    }

    const btn = document.getElementById("autoFixBtn");

    btn.disabled = true;
    btn.innerText = "Fixing...";

    try {

        const response = await fetch(API + "/bugfix/project", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                project_path: projectPath

            })

        });

        const data = await response.json();

        console.log(data);

        if (data.status === "success") {


            const downloadBtn =
                document.getElementById("downloadFixedBtn");

            downloadBtn.style.display = "inline-block";

            downloadBtn.onclick = function () {

                window.open(

                    API +
                    "/bugfix/download?path=" +
                     encodeURIComponent(data.download_url)

                 );

            };

            alert(
                "✅ " +
                data.fixed_files +
                " files fixed successfully."
            );

        } else {

            alert("Fix Failed");

        }
    }

    catch(err){

        console.error(err);

        alert("Server Error");

    }

    btn.disabled = false;

    btn.innerText = "🛠 Auto Fix Bugs";

}