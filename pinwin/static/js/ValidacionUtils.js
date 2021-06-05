const validables = document.getElementsByClassName("validate");
const submitBtn = document.getElementById("submit");
submitBtn.disabled = true;

(function ValidacionInit($) {
    const password = $("#password");
    const passwordConfirm = $("#passwordConfirm");

    password.on("input", function () {
        if (password.val() !== passwordConfirm.val()) {
            passwordConfirm.removeClass("valid").addClass("invalid");
        } else {
            passwordConfirm.removeClass("invalid").addClass("valid");
        }
    });

    passwordConfirm.on("input", function () {
        if (passwordConfirm.val() !== password.val()) {
            $(this).removeClass("valid").addClass("invalid");
        } else {
            $(this).removeClass("invalid").addClass("valid");
        }
    });

    for (let i = 0; i < validables.length; i++) {
        console.log(validables[i]);
        validables[i].addEventListener("input",  EnablearBotonSiEsValido);
        validables[i].addEventListener("focusout", EnablearBotonSiEsValido);
    }

})(jQuery);

function EnablearBotonSiEsValido() {
    let validos = document.getElementsByClassName("valid");
    console.log(validos.length);
    submitBtn.disabled = validos.length !== validables.length;

}
