// ==========================
// Login Check
// ==========================

const token = localStorage.getItem("token");

if (!token) {
    window.location.href = "/login";
}

// ==========================
// Dashboard
// ==========================

async function loadDashboard() {

    try {

        // Latest Report
        const reportResponse = await fetch("http://127.0.0.1:8000/reports/", {
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });

        const reports = await reportResponse.json();

        if (reports.length > 0) {

            const result = reports[0];

            document.getElementById("qualityScore").innerText =
                result.score || 0;

            document.getElementById("securityScore").innerText =
                80;

            let coverage = 0;

            try {

                const cov = JSON.parse(result.coverage);

                coverage = cov.coverage_percent || 0;

            } catch {}

            document.getElementById("coverage").innerText =
                coverage + "%";

            try {

                const analysis = JSON.parse(result.analysis_json);

                document.getElementById("bugs").innerText =
                    analysis.total_bugs || 0;

            } catch {

                document.getElementById("bugs").innerText = 0;

            }

            document.getElementById("report").innerText =
                result.final_report || "No Report";
        }

        // Dashboard Stats
        const statsResponse = await fetch(
            "http://127.0.0.1:8000/dashboard/stats",
            {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            }
        );

        const stats = await statsResponse.json();

        document.getElementById("totalProjects").innerText =
            stats.total_projects;

        document.getElementById("totalReports").innerText =
            stats.total_reports;

        document.getElementById("averageScore").innerText =
            stats.average_score + "%";

        document.getElementById("lastScan").innerText =
            stats.last_scan;

    }

    catch (err) {

        console.log(err);

    }

}

window.onload = loadDashboard;

// ==========================
// Logout
// ==========================

document.addEventListener("DOMContentLoaded", () => {

    const logoutBtn = document.getElementById("logoutBtn");

    logoutBtn.onclick = function () {

        if (!confirm("Logout?")) return;

        localStorage.removeItem("token");

        window.location.href = "/login";

    };

});