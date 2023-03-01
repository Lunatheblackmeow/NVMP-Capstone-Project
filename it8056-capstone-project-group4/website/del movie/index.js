$(document).ready(
    function () {
        if (localStorage.getItem("JWT")==null) {
            $("#pagemsg").html("<center><p>Sorry, please log in first!</p></center>");
        }
        else {
            $("#pagemsg").html("<center><p>Login successful!</p></center>");
        }
        $('#btnDelMovie').click(function () {
            const input = $('#txtMovieId').val();
            alert("Are you sure you want to delete movie "+input+"?");
                $.ajax({
                    url: 'http://127.0.0.1:5000/movies/'+input,
                    type: 'DELETE',
                    headers: {
                    Authorization: "Bearer "+localStorage.getItem("JWT")
                    },
                    success: function (response) {
                        console.log(response);
                        alert("Movie "+input+" deleted.");
                    },
                    error: function (err) {
                        console.log(err);
                        if (err.status==403) {
                            alert("Sorry! Only admins can delete movies!");
                        }
                        else {
                            alert("Error! Unable to delete the movie!");
                        }
                    }
                });
        });
        $('#btnGetMovieListing').click(function () {
            $.get(`http://127.0.0.1:5000/movies`)
                .done(function (data) {
                    const selector = $('#movie-detail-all');
                    selector.text(JSON.stringify(data['Movies']));
                })
                .catch(function (error) {
                    alert('ERROR!');
                    const selector = $('#movie-detail-all');
                    selector.text(JSON.stringify(error.responseJSON.error));
                    console.error('Failed to connect to backend! Error: ', error);
                });
        })
    }
);
/*
UPDATE
$.ajax({
url: 'http://127.0.0.1:5000/movie/'+id,
type: 'PUT',
contentType: 'application/json',
data: JSON.stringify(data),
success: function (response) {
    console.log(response);
},
error: function (err) {
    console.log(err);
}
});

CREATE/INSERT/LOGIN
$.ajax({
    url: 'http://127.0.0.1:5000/movie',
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(data),
    success: function (response) {
        console.log(response);
    },
    error: function (err) {
        console.log(err);
    }
});
$.post({
    url: 'http://127.0.0.1:5000/movie',
    data: JSON.stringify({
        'name': NameTextbox,
        'description': DescriptBox,
        'price': PriceBox,
        'country': CountryBox,
        'travelPeriod': DaysBox,
        'type': type
    }),
    headers: {
        "Content-Type": "application/json" // Tell the server, to treat the body as JSON
    },
}).done(function(data) {
    console.log("Data Loaded: " + data);
  })
  .fail(function(xhr, status, error) {
    console.log("Error: " + xhr.responseText);
  });

DELETE
$.ajax({
    url: 'http://127.0.0.1:5000/movie/'+id,
    type: 'DELETE',
    success: function (response) {
        console.log(response);
    },
    error: function (err) {
        console.log(err);
    }
});
*/

