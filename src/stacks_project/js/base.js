$(document).ready(function () {

    //Toggling between login and register forms
    let loginDiv = $('.log');
    let registerDiv = $('.reg');
    registerDiv.hide();
    $('.toggler-button').on('click', function () {
        $('.log,.reg').toggle();
    });
    // End Of toggling

});