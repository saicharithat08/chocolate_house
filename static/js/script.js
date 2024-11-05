document.addEventListener("DOMContentLoaded", () => {
    fetchFlavors();

    const form = document.getElementById("flavorForm");
    form.addEventListener("submit", (e) => {
        e.preventDefault();
        addFlavor();
    });
});

// Fetch all flavors from the API
function fetchFlavors() {
    fetch("/flavors")
        .then(response => response.json())
        .then(data => {
            const flavorsList = document.getElementById("flavorsList");
            flavorsList.innerHTML = "";
            data.forEach(flavor => {
                const flavorItem = document.createElement("div");
                flavorItem.className = "flavor-item";
                flavorItem.innerHTML = `
                    <strong>${flavor.name}</strong> - ${flavor.description || "No description"}
                    <br>Available: ${flavor.available ? "Yes" : "No"}
                `;
                flavorsList.appendChild(flavorItem);
            });
        })
        .catch(error => console.error("Error fetching flavors:", error));
}

// Add a new flavor to the API
function addFlavor() {
    const name = document.getElementById("flavorName").value;
    const description = document.getElementById("flavorDescription").value;
    const available = document.getElementById("flavorAvailable").checked;

    fetch("/flavors", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name, description, available })
    })
    .then(response => {
        if (response.status === 201) {
            fetchFlavors();
            document.getElementById("flavorForm").reset();
        } else {
            console.error("Failed to add flavor");
        }
    })
    .catch(error => console.error("Error adding flavor:", error));
}
