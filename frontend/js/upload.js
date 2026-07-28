// ==========================
// Upload Project
// ==========================

document.addEventListener("DOMContentLoaded", () => {

    const uploadBtn = document.getElementById("uploadBtn");

    if (uploadBtn) {

        uploadBtn.addEventListener("click", uploadProject);

    }

});

async function uploadProject() {

    const fileInput = document.getElementById("zipFile");

    if (!fileInput.files.length) {

        alert("Please select ZIP file.");

        return;

    }

    const file = fileInput.files[0];

    const formData = new FormData();

    formData.append("file", file);

    try {

        uploadBtn.disabled = true;
        uploadBtn.innerText = "Uploading...";

        const response = await fetch(`${API}/upload/zip`, {

            method: "POST",

            body: formData

        });

        const data = await response.json();

        console.log("UPLOAD RESPONSE", data);

        if (data.status !== "success") {

            alert(data.detail || "Upload Failed");

            uploadBtn.disabled = false;
            uploadBtn.innerText = "Upload ZIP";

            return;

        }

        // ==========================
        // Save Project Details
        // ==========================

        localStorage.setItem("project_id", data.project_id);

        localStorage.setItem("project_name", data.project_name);

        localStorage.setItem("project_path", data.project_path);

        alert("Project Uploaded Successfully ✅");

        uploadBtn.disabled = false;
        uploadBtn.innerText = "Upload ZIP";

    }

    catch (err) {

        console.error(err);

        alert("Server Error");

        uploadBtn.disabled = false;
        uploadBtn.innerText = "Upload ZIP";

    }

}