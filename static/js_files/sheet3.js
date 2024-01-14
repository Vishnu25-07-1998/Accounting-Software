function validateForm(){
    var startDate = document.getElementById("startdate").value;
    var endDate = document.getElementById("enddate").value;

    // Check if either start date or end date is empty
    if (!startDate || !endDate) {
        alert("Please enter both start and end dates.");
        return false;  // Prevent form submission
    }

    return true;  // Allow form submission
}

$(document).ready(function () {
    $('.datepicker').datepicker({
        format: 'yyyy-mm-dd', // set your desired date format
        autoclose: true,
    });
});