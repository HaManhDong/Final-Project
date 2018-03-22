'use strict';

$(document).ready(function () {
    $('#dashboard').click();
    $.get(OPENHAB_API_ITEMS, function (res, status, req) {
        if (req.getResponseHeader('Content-Type') == 'application/json') {
            $('#number-of-devices-box').html(res.length);
        } else {
            $('#number-of-devices-box').html(-1);
        }
    })

    let options = {
        clientId: 'pas',
        connectTimeout: MQTT_CONNECT_TIMEOUT,
        hostname: MQTT_HOSTNAME,
        port: MQTT_PORT,
        path: MQTT_PATH
    };

    let client = mqtt.connect(options);

    client.on('connect', function () {
        client.subscribe('a');
        // client.publish('a', 'Hello mqtt')
    });

    client.on('message', function (topic, message) {
        console.log(message.toString());
        $('.add-user-panel').find('div.overlay i').css('display', 'none');
        $('.add-user-panel').find('div.rfid-card-id strong').css('display', '').html(message.toString());
        $('#btn-scan-rfid').removeAttr('disabled').html('Re-scan');
    });

    $('#btn-scan-rfid').on('click', scan_rfid_card);

});

function scan_rfid_card() {
    $('.add-user-panel').find('div.overlay i').css('display', '');
    $('.add-user-panel').find('div.rfid-card-id strong').css('display', 'none');
    $(this).attr('disabled', 'disabled');
}