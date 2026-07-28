// ==========================
// Charts
// ==========================

let bugChart = null;
let qualityChart = null;

function loadCharts() {

    // Safe LocalStorage Read
    const stored = localStorage.getItem("analysis");

    if (!stored || stored === "undefined") {
        return;
    }

    let analysis;

    try {
        analysis = JSON.parse(stored);
    } catch (e) {
        console.error("Invalid Analysis JSON");
        return;
    }

    //-------------------------
    // Bug Chart
    //-------------------------

    const totalBugs = analysis.total_bugs || 0;

    const totalFiles =
        (analysis.file_reports || []).length;

    const safeFiles =
        Math.max(totalFiles - totalBugs, 0);

    const bugCtx =
        document.getElementById("bugChart");

    if (bugCtx) {

        if (bugChart)
            bugChart.destroy();

        bugChart = new Chart(bugCtx, {

            type: "doughnut",

            data: {

                labels: [

                    "Bugs",

                    "Clean Files"

                ],

                datasets: [

                    {

                        data: [

                            totalBugs,

                            safeFiles

                        ],

                        backgroundColor: [

                            "#ef4444",

                            "#22c55e"

                        ]

                    }

                ]

            },

            options: {

                responsive: true,

                plugins: {

                    legend: {

                        position: "bottom"

                    }

                }

            }

        });

    }

    //-------------------------
    // Quality Chart
    //-------------------------

    const quality =
        analysis.project_score || 0;

    const security =
        analysis.security_score || 0;

    let coverage = 0;

    if (typeof analysis.coverage === "object") {

        coverage =
            analysis.coverage.coverage_percent || 0;

    }

    const qualityCtx =
        document.getElementById("qualityChart");

    if (qualityCtx) {

        if (qualityChart)
            qualityChart.destroy();

        qualityChart = new Chart(qualityCtx, {

            type: "bar",

            data: {

                labels: [

                    "Quality",

                    "Security",

                    "Coverage"

                ],

                datasets: [

                    {

                        label: "Score",

                        data: [

                            quality,

                            security,

                            coverage

                        ],

                        backgroundColor: [

                            "#2563eb",

                            "#16a34a",

                            "#f59e0b"

                        ]

                    }

                ]

            },

            options: {

                responsive: true,

                scales: {

                    y: {

                        beginAtZero: true,

                        max: 100

                    }

                }

            }

        });

    }

}

// ==========================
// Auto Load
// ==========================

document.addEventListener("DOMContentLoaded", () => {

    loadCharts();

});