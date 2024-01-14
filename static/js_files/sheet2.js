function toggleDateSelection() {
    var bankSelect = document.getElementById("BankName");
    var dateSelectionSection = document.getElementById("dateSelectionSection");

    // Check if the selected bank is "VFD Bank"
    if (bankSelect.value === "ZFS Bank") {
        dateSelectionSection.style.display = "block";  // Show the date range section
    } else {
        dateSelectionSection.style.display = "none";   // Hide the date range section
        alert('Transaction for Selected Bank doesnt exists');
    }
}


function validateForm() {
    var startDate = document.getElementById("startdate").value;
    var endDate = document.getElementById("enddate").value;

    // Check if either start date or end date is empty
    if (!startDate || !endDate) {
        alert("Please enter both start and end dates.");
        return false;  // Prevent form submission
    }

    return true;  // Allow form submission
}