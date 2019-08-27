var tstart= '<table><thead><tr><th>Answer ID</th><th>Answer </th><th> Related to Post</th></tr></thead><tbody>'
var tend= '</tbody></table>'


$(document).ready(function() {
    $('#get-data').click(function () {
        alert("clicked")
        $.ajax({
            url: "http://127.0.0.1:8000/rest-api/choices/"+$('#choice_number').val()+"/",
            type: 'GET',
            success: function (data) {
                $( "strong" ).text( data.poll );
                $( "i" ).text( data.choice_text );
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("Error: " + errorThrown);
            }
        });
    });
    $("#put-data").click(function () {
        $.ajax({
            url: "http://127.0.0.1:8000/rest-api/choices/"+$('#choice_number').val()+"/",
            type: 'PUT',
            data: {poll:$('#poll').val(), choice_text:$('#choice').val()},
            success: function(data) {
                alert("Your Data has been PUT Successfully");
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("Error: " + errorThrown);
            }
        });

        // or we might do $.post( "http://127.0.0.1:8000/rest-api/choices/2", $( "#choice-form" ).serialize() );

    })

    $('#get-list').click(function () {
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
                $('div').html(tstart+text+tend)
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("Error: " + errorThrown);
            }
        });
    })
    $("#new-list-form").submit(function (e) {
        e.preventDefault();
        $.ajax({
           type: "POST",
           url: "http://127.0.0.1:8000/rest-api/choices/",
           data: $(this).serialize(), // serializes the form's elements.
           success: function(data)
           {
               console.log(data);
           },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("Error: " + errorThrown);
            }

         });

    })
})