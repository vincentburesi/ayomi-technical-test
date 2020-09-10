function formSubmitter(form) {
    let alertContainer = $("#alertPlaceholder");
    let alert = {
        success: function(message) {
            alertContainer.html('<div class="alert alert-success">' +
                '<a class="close" data-dismiss="alert">&times;</a><span>' + message + '</span></div>')
        },
        error: function(message) {
            alertContainer.html('<div class="alert alert-danger">' +
                '<a class="close" data-dismiss="alert">&times;</a><span>' + message + '</span></div>')
        },
    };

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        submitForm(form);
    });

    function submitForm(form) {
        let xhr = new XMLHttpRequest();
        let formData = new FormData(form)

        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    alert.success("Saved changes!");
                } else {
                    alert.error("Error " + xhr.status + ": " + xhr.response);
                }
            }
        }

        xhr.open("POST", "");
        xhr.send(formData);
    }
}
