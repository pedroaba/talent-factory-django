$(document).ready(function () {
    const queryParams = new URLSearchParams(window.location.search)
    const situation = queryParams.get("carType")
    $(`#${situation}`).prop("checked", true)
})