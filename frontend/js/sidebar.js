window.addEventListener("load", () => {

    setupSidebar();

    setupTheme();

});

function setupSidebar() {

    const items = document.querySelectorAll("#sidebarMenu li");

    items.forEach(item => {

        item.addEventListener("click", () => {

            // Logout button ko ignore karo
            if (item.id === "logoutBtn") return;

            items.forEach(i => i.classList.remove("active"));

            item.classList.add("active");

            const target = item.dataset.target;

            if (!target) return;

            document.getElementById(target)?.scrollIntoView({

                behavior: "smooth"

            });

        });

    });

}

function setupTheme() {

    const btn = document.getElementById("themeBtn");

    if (!btn) return;

    btn.onclick = () => {

        document.body.classList.toggle("dark");

    };

}