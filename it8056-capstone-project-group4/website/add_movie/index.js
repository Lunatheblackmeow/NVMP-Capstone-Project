$(document).ready(function() {
    if (localStorage.getItem("JWT")==null) {
        $("#pagemsg").html("<center><p>Sorry, please log in first!</p></center>");
    }
    else {
        $("#pagemsg").html("<center><p>Login successful!</p></center>");
    }

    $("#addmoviebtn").click(function(evt) {

        evt.preventDefault();

        const thetitle=$("#movietitle").val();
        const thedescrp=$("#moviedescrp").val();
        const thedate=$("#moviedate").val();
        const thegenre=$("#genreid").val();

        if ((thetitle=="")||(thedescrp=="")||(thedate=="")||(thegenre=="")) {
            alert("Please fill up all the fields!");
            return;
        }

        const data={
            "moviename": thetitle,
            "description": thedescrp,
            "releasedate": thedate,
            "genreid": thegenre
        };

        $.ajax({
            url: "http://127.0.0.1:5000/add_movie",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(data),
            headers: {
                Authorization: "Bearer "+localStorage.getItem("JWT")
            },
            success: function(response) {
                console.log(response);
                alert("Movie added!");
            },
            error: function(err) {
                console.log(err);
                if (err.status==403) {
                    alert("Sorry! Only admins can add movies!");
                    $("#pagemsg").html("<center><p>Login successful!<br>However, you have to be an <b>admin</b> to update a movie.</p></center>");
                }
                else {
                    alert("Error! Unable to add the movie!");
                }
            }
        });

    });
});