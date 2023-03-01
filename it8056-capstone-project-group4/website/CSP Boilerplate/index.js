window.onload = function () {
    $.get('https://api.data.gov.sg/v1/environment/air-temperature')
        .done(function (data) {
            const allReadings = data.items[0].readings;
            let totalTemperature = 0;
            for (let i = 0; i < allReadings.length; i++) {
                totalTemperature += allReadings[i].value;
            }
            const averageTemperature = totalTemperature / allReadings.length;
            document.querySelector('#temperature').textContent = averageTemperature;

            if (averageTemperature < 28) {
                document.getElementById('emoji').textContent = '🥶';
            } else if (averageTemperature < 32) {
                document.getElementById('emoji').innerHTML = '😃';
            } else {
                $('#emoji').text('🥵');
            }
        })
        .catch(function (error) {
            console.error('Failed to connect to backend! Error: ', error);
        });
};
