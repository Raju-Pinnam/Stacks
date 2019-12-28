$(document).ready(function () {

    let loginDiv = $('.log');
    let registerDiv = $('.reg');

    $('.toggler-button').click(function () {
        if (loginDiv.css('display') === 'none') {
            loginDiv.show();
            registerDiv.hide()
        }
        if (registerDiv.css('display') === 'none') {
            registerDiv.show();
            loginDiv.hide()
        }
    });

    $('.nav-button-tog').click(function () {
        $('.nav-button-tog').toggleClass('change')
    });

    // $(window).scroll(function () {
    //     let position = $(this).scrollTop();
    //     console.log(position)
    // });

    //Toggling between login and register forms

    // End Of toggling

});