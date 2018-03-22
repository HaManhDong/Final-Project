'use strict';

let OPENHAB_API_ITEMS = "http://localhost:8080/rest/items";

let MQTT_CONNECT_TIMEOUT = 5000;
let MQTT_HOSTNAME = "broker.hivemq.com";
let MQTT_PORT = 8000;
let MQTT_PATH = "/mqtt";

$('.pas-sidebar-element').each(function (index) {
    $(this).on('click', function () {
        if (!$(this).hasClass('active')) {
            $('ul.sidebar-menu li.pas-sidebar-element.active').removeClass('active');
            $(this).addClass('active');
        }
    })
});

let create_datatables_info = function (selector, data, columns) {
    return $('#' + selector).DataTable({
        data: data,
        columns: columns
    });
};

