$(document).ready(function () {
    function formatFileSizeInMb(filesize) {
        const fileSizeInMb = filesize / (1024 * 1024);
        const roundedFileSizeInMb = fileSizeInMb.toFixed(2);

        return roundedFileSizeInMb + " MB";
    }

    $("#id_photo_car").on("change", function (event) {
        const files = event.target.files

        $("#file").remove()
        for (const file of files) {
            const blobUrl = URL.createObjectURL(file)
            const fileElement = $(`
                <div id="file" class="w-full hidden mt-2 py-1 px-2 relative">
                    <img src="${blobUrl}" alt="" class="cover w-full" />
                </div>
            `)

            $("#file-container").append(fileElement)
            fileElement.slideDown()
        }
    })
})