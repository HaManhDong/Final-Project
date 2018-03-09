'use strict';

$(document).ready(function () {
    $('#dashboard').click();
    $.get('http://localhost:8080/rest/items', function (res, status, req) {
        if (req.getResponseHeader('Content-Type') == 'application/json') {
            $('#number-of-devices-box').html(res.length);
        } else {
            $('#number-of-devices-box').html(-1);
        }
    })

    // Create a client instance
    let client = new Paho.MQTT.Client('localhost', 1883, "pas");

    // set callback handlers
    client.onConnectionLost = onConnectionLost;
    client.onMessageArrived = onMessageArrived;

    console.log(client);
    // connect the client
    client.connect({onSuccess: onConnect});


    // called when the client connects
    function onConnect() {
        // Once a connection has been made, make a subscription and send a message.
        console.log("onConnect");
        client.subscribe("a");
        let message = new Paho.MQTT.Message("Hello, from PAS");
        message.destinationName = "World";
        client.send(message);
    }

    // called when the client loses its connection
    function onConnectionLost(responseObject) {
        if (responseObject.errorCode !== 0) {
            console.log("onConnectionLost:" + responseObject.errorMessage);
        }
    }

    // called when a message arrives
    function onMessageArrived(message) {
        console.log("onMessageArrived:" + message.payloadString);
    }
});