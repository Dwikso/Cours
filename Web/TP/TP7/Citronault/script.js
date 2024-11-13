document.getElementById('valider').addEventListener('click', function(event) {
    event.preventDefault();

    let basePrice = 16400;
    let motorisation = document.getElementById('motorisation').value;
    let type = document.querySelector('input[name="type"]:checked').value;
    let climatisation = document.getElementById('climatisation').checked;
    let peinture = document.getElementById('peinture').checked;
    let autoRadio = document.getElementById('auto-radio').checked;

    if (motorisation === 'essence 1.6') {
        basePrice += 2000;
    } else if (motorisation === 'DCI') {
        basePrice += 3000;
    }

    if (type === '5portes') {
        basePrice += 1000;
    }

    if (climatisation) {
        basePrice += 2000;
    }

    if (peinture) {
        basePrice += 300;
    }

    if (autoRadio) {
        basePrice += 100;
    }

    document.getElementById('res').textContent = basePrice + '€';
});