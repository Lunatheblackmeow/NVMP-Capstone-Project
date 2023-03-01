function loadDadJoke() {
    fetch('https://icanhazdadjoke.com/', {
        headers: {
            // specific for this API to tell them to give us the data in JSON format
            Accept: 'application/json',
        },
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            $('#dad-joke').html(`<p>${data.joke}</p>`);
        });
}

$(function () {
    loadDadJoke();

    document.getElementById('refresh').onclick = loadDadJoke;
});
