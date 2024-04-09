$(document).ready(function () {
    setTimeout(() => {
        const queryParams = new URLSearchParams(window.location.search)
        const situation = queryParams.get("carType")
        $(`#${situation}`).attr("checked", true)
    }, 100)
})