$(document).ready(function () {
    //This will present credentials of User and get the User Token Field
    $('#login').click(function () {
        //Send a POST Request to the URL for Token specified for User
        var user = $('#username').val()
        $.ajax({
            type: 'POST',
            data: {
                username: user,
                password: $('#password').val()
            },
            url: 'http://127.0.0.1:8000/rest-api/api-token-auth/',
            success: function (res) {
                console.log(res.token)
                sessionStorage.setItem(user, res.token)
                sessionStorage.setItem('currUser', user)
                //Initialize the Ajax for the first time
                $.ajaxSetup({
                    //Set the headers so that these will be in every HTTP Request
                    headers: {
                        "Authorization": 'Token ' + sessionStorage.getItem(sessionStorage.getItem('currUser'))
                    }
                });
                window.location.href="Polls,Choices%20API.html";
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert("Error: " + errorThrown);
            }
        });
    });
});