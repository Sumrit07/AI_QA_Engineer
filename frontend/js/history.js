// ==========================
// History
// ==========================

let allReports = [];
let showingAll = false;
let hasScrolledToHistory = false;

async function loadHistory() {

    const tbody = document.querySelector("#historyTable tbody");

    if (!tbody) return;

    tbody.innerHTML = `
    <tr>
        <td colspan="6" style="text-align:center">
            Loading...
        </td>
    </tr>`;

    try {

        const response = await fetch(`${API}/reports/`);

        allReports = await response.json();

        renderHistory();

    }

    catch (err) {

        console.error(err);

        tbody.innerHTML = `
        <tr>
            <td colspan="6" style="text-align:center;color:red">
                Failed To Load History
            </td>
        </tr>`;

    }

}

// ==========================
// Render History
// ==========================

function renderHistory() {

    const tbody = document.querySelector("#historyTable tbody");

    tbody.innerHTML = "";

    if (!allReports || allReports.length === 0) {

        tbody.innerHTML = `
        <tr>
            <td colspan="6" style="text-align:center">
                No History Found
            </td>
        </tr>`;

        return;

    }

    let reports = [...allReports];

    const keyword = document
        .getElementById("historySearch")
        ?.value
        ?.trim()
        ?.toLowerCase() || "";

    if (keyword) {

        reports = reports.filter(report =>

            report.project_name &&
            report.project_name
                .toLowerCase()
                .includes(keyword)

        );

    }

     
                    

if (!showingAll) {

    reports = reports.slice(0, 5);

}

    reports.forEach(report => {

        let coverage = report.coverage;

        if (typeof coverage === "object") {

            coverage =
                coverage.coverage_percent + "%";

        }

        tbody.innerHTML += `

        <tr>

            <td>${report.project_name || "-"}</td>

            <td>${report.score || 0}</td>

            <td>${coverage || "0%"}</td>

            <td>${report.total_files || 0}</td>

            <td>${new Date(report.created_at).toLocaleString()}</td>

            <td>

                <button
                    onclick="deleteHistory(${report.id})">

                    🗑 Delete

                </button>

            </td>

             <td>
                <button onclick="viewReport(${report.id})">
                    👁 View
                </button>
            </td>

        </tr>

        `;

    });

    createHistoryButton();

}

// ==========================
// View All Button
// ==========================

function createHistoryButton() {

    let oldBtn =
        document.getElementById("viewAllHistory");

    if (oldBtn) {

        oldBtn.remove();

    }

    if (allReports.length <= 5)
        return;

    const btn = document.createElement("button");

    btn.id = "viewAllHistory";

    btn.style.marginTop = "15px";

    btn.innerText = showingAll
        ? "Show Less"
        : "View All History";

    btn.onclick = function () {

        showingAll = !showingAll;

        renderHistory();

    };

    document
        .querySelector("#historySection")
        .appendChild(btn);

}

// ==========================
// Delete History
// ==========================

async function deleteHistory(id) {

    const ok = confirm(
        "Delete this report?"
    );

    if (!ok) return;

    try {

        const response = await fetch(

            `${API}/reports/${id}`,

            {

                method: "DELETE"

            }

        );

        const data = await response.json();

        if (data.status === "success") {

            alert("Deleted Successfully");

            loadHistory();

        }

        else {

            alert("Delete Failed");

        }

    }

    catch (err) {

        console.error(err);

        alert("Server Error");

    }

}

// ==========================
// Auto Load
// ==========================
document.addEventListener("DOMContentLoaded", () => {

    loadHistory();

    const searchBox = document.getElementById("historySearch");

    if (searchBox) {

        searchBox.addEventListener("input", () => {

            if (searchBox.value.trim() === "") {

                hasScrolledToHistory = false;
            }

            if (!hasScrolledToHistory && searchBox.value.trim() !== "") {

                document.getElementById("historySection").scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });

                searchBox.blur();

                hasScrolledToHistory = true;
            }

            renderHistory();

        });

    }

});



// ==========================
// View Report
// ==========================

async function viewReport(reportId) {

    try {

        const response = await fetch(`${API}/reports/${reportId}`);

        const data = await response.json();

        if (data.status !== "success") {
            alert("Report Not Found");
            return;
        }

        const report = data.report;

        // -------------------------
        // Quality Score
        // -------------------------
        document.getElementById("qualityScore").innerText =
            report.score || "--";

        // -------------------------
        // Coverage
        // -------------------------
        let coverage = report.coverage;

        try {

            coverage = JSON.parse(
                coverage.replace(/'/g, '"')
            );

            document.getElementById("coverage").innerText =
                (coverage.coverage_percent || 0) + "%";

        }

        catch {

            document.getElementById("coverage").innerText =
                coverage || "--";

        }

        // -------------------------
        // Final Report
        // -------------------------
        document.getElementById("report").innerText =
            report.final_report || "No Report";

        // -------------------------
        // Load Full Analysis (NEW)
        // -------------------------
        if (report.analysis_json) {

            document.getElementById("securityScore").innerText =
                report.analysis_json.security_score ?? "--";

            document.getElementById("bugs").innerText =
                report.analysis_json.total_bugs ?? 0;

            document.getElementById("qualityScore").innerText =
                report.analysis_json.project_score ?? report.score;

            if (typeof fillBugTable === "function")
                fillBugTable(report.analysis_json);

            if (typeof fillSecurityTable === "function")
                fillSecurityTable(report.analysis_json);

            if (typeof fillPerformanceTable === "function")
                fillPerformanceTable(report.analysis_json);

            if (typeof fillSmellTable === "function")
                fillSmellTable(report.analysis_json);

        }

        document.getElementById("reportSection")
            .scrollIntoView({
                behavior: "smooth"
            });

        alert("Report Loaded Successfully");

    }

    catch (err) {

        console.error(err);

        alert("Failed To Load Report");

    }

}