'use strict';

let OPENHAB_API_ITEMS = "http://localhost:8080/rest/items";

let MQTT_CONNECT_TIMEOUT = 5000;
let MQTT_HOSTNAME = "broker.hivemq.com";
let MQTT_PORT = 8000;
let MQTT_PATH = "/mqtt";
let MQTT_TOPIC_USER_REGISTER = "pas/mqtt/rfid/user_register";

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


window.setTimeout(function() {
  $(".alert").fadeTo(500, 0).slideUp(500, function(){
      $(this).remove();
  });
}, 5000);