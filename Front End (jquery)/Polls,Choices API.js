var tstart= '<table><thead><tr><th>ID</th><th>Question </th><th>Created By</th></tr></thead><tbody>'
var tend= '</tbody></table>'

var t2start= '<table><thead><tr><th>Answer ID</th><th>Answer </th><th> Related to Post</th></tr></thead><tbody>'
var t2end= '</tbody></table>'


$(document).ready(function () {
        $.ajaxSetup({
            //Set the headers so that these will be in every HTTP Request
            headers: {
                "Authorization": 'Token ' + sessionStorage.getItem(sessionStorage.getItem('currUser'))
            }
        });
    $('.poll #get-data').click(function () {
        console.log(sessionStorage.getItem(sessionStorage.getItem('currUser')))
        $.ajax({
            url: "http://127.0.0.1:8000/rest-api/polls/"+$('.poll #poll_number').val()+"/",
            type: 'GET',
            success: function (data) {
                $( ".poll i" ).text( data.question );
                $( '.poll strong' ).text( data.created_by );
                $('.poll #question').val(data.question);
                $('.poll #asked_by').val(data.created_by)

            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("Error: " + errorThrown);
            }
        });
    });

    $(".poll #put-data").click(function () {
        $.ajax({
            url: "http://127.0.0.1:8000/rest-api/polls/"+$('.poll #poll_number').val()+"/",
            type: 'PUT',
            data: {question:$('.poll #question').val(), created_by:$('.poll #asked_by').val()},
            success: function(data) {
                $('.poll #get-polls-list').click();

            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("Error: " + errorThrown);
            }
        });

        // or we might do $.post( "http://127.0.0.1:8000/rest-api/choices/2", $( "poll #choice-form" ).serialize() );

    })

    $('.poll #get-polls-list').click(function () {
        $.ajax({
            url: "http://127.0.0.1:8000/rest-api/polls/list/",
            type: 'GET',
            success: function (data) {
                var i, text='';
                for (i=0; i <data.length; i++){
                    text += '<tr><td> '+data[i].id+' </td>'+
                        '<td> ' + data[i].question + ' </td>' +
                        '<td> '+data[i].created_by+' </td></tr>';
                }
                $('.polls-list').html(tstart+text+tend)
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("Error: " + errorThrown);
            }
        });
    })

    $(".poll #new-list-form").submit(function (e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/rest-api/polls/list/",
            data: $(this).serialize(), // serializes the form's elements.
            success: function(data)
            {
                alert("New Poll Created");
                $('.poll #get-polls-list').click();

            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("Error: " + errorThrown);
            }

        });

    })

    // Choice API
    // Starts From Here
    //All the Functions


    $('.choice #get-choice').click(function () {
        $.ajax({
            url: "http://127.0.0.1:8000/rest-api/choices/"+$('.choice #choice_number').val()+"/",
            type: 'GET',
            success: function (data) {
                $( ".choice strong" ).text( data.poll );
                $( ".choice i" ).text( data.choice_text );
                $('.choice #poll').val(data.poll);
                $('.choice #choice').val(data.choice_text)

            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("Error: " + errorThrown);
            }
        });
    });

    $(".choice #put-choice-data").click(function () {
        $.ajax({
            url: "http://127.0.0.1:8000/rest-api/choices/"+$('.choice #choice_number').val()+"/",
            type: 'PUT',
            data: {poll:$('.choice #poll').val(), choice_text:$('.choice #choice').val()},
            success: function(data) {
                alert("List Updated");
                $('.choice #get-choice-list').click()
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("Error: " + errorThrown);
            }
        });

    })

    $('.choice #get-choice-list').click(function () {
        $.ajax({
            url: "http://127.0.0.1:8000/rest-api/choices/",
            type: 'GET',
            success: function (data) {
                var i, text='';
                for (i=0; i <data.length; i++){
                    text += '<tr><td> '+data[i].id+' </td>'+
                        '<td> ' + data[i].choice_text + ' </td>' +
                        '<td> '+data[i].poll+' </td></tr>';
                }
                $('.choice-list').html(t2start+text+t2end)
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("Error: " + errorThrown);
            }
        });
    })
    $(".choice #new-choice-form").submit(function (e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/rest-api/choices/",
            data: $(this).serialize(), // serializes the form's elements.
            success: function(data)
            {
                alert("Item Created");
                $('.choice #get-choice-list').click()
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("Error: " + errorThrown);
            }

        });

    })
});