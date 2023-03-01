
$(document).ready(
    function () {
        $('#btnGetMovie').click(function () {
            const input = $('#txtMovieId').val();
            $.get(`http://127.0.0.1:5000/movies/byid/${input}`)
                .done(function (data) {
                    const var_description = $('#tr_description');
                    var_description.text(JSON.stringify(data.Movies[0].description));
                    const var_genreID = $('#tr_genreID');
                    var_genreID.text(JSON.stringify(data.Movies[0].genreid));
                    const var_movieID = $('#tr_movieID');
                    var_movieID.text(JSON.stringify(data.Movies[0].movieid));
                    const var_name = $('#tr_name');
                    var_name.text(JSON.stringify(data.Movies[0].moviename));
                    const var_release_date = $('#tr_release_date');
                    var_release_date.text(JSON.stringify(data.Movies[0].releasedate));
                })
                .catch(function (error) {
                    alert('ERROR!');
                    const selector = $('#movie-detail');
                    selector.text(JSON.stringify(error.responseJSON.error));
                    console.error('Failed to connect to backend! Error: ', error);
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

