'use strict';

$(document).ready(function () {

    $('#id_card_id').removeAttr('required').parent().css('display', 'none');

    $('#members-info').click();

    $('#pas_datatables_members_info').DataTable({
        "dom": 'lf<"#btn_add_member_container">rtip'
    });
    $('#btn_add_member_container').css("float", "right");
    $('#btn_add_member').appendTo('#btn_add_member_container')
        .css({marginRight: "10px", marginBottom: "15px"});

    $.get('/pas/api/members', function (res, status, req) {
        console.log(res);
    });

    $('#btn-scan-rfid').on('click', scan_rfid_card);
    submit_new_member_event();

    $('#btn_edit_member').on('click', function () {
        // alert('ok');
    })
});

function scan_rfid_card() {

    $('#id_card_id_container').find('div p i').css('display', '');
    $('#id_card_id_temp').css('display', 'none');
    $(this).attr('disabled', 'disabled');
    $('#btn_submit_new_memeber').attr('disabled', 'disabled');

    // MQTT client
    let options = {
        clientId: 'pas',
        connectTimeout: MQTT_CONNECT_TIMEOUT,
        hostname: MQTT_HOSTNAME,
        port: MQTT_PORT,
        path: MQTT_PATH
    };

    let client = mqtt.connect(options);

    client.on('connect', function () {
        client.subscribe(MQTT_TOPIC_USER_REGISTER);
    });

    client.on('message', function (topic, message) {
        $('#id_card_id_container').find('div p i').css('display', 'none');
        $('#id_card_id_temp').css('display', '').html(message.toString());
        $('#btn-scan-rfid').removeAttr('disabled').html('Re-scan');
        $('#btn_submit_new_memeber').removeAttr('disabled');
        client.end();
    });
}

function submit_new_member_event() {
    $("#new_member_form").submit(function (event) {

        let card_id = $('#id_card_id_temp').text();
        if(card_id){
            console.log(card_id);
            $('#id_card_id').val(card_id);
        } else {
            alert('Miss card ID!');
            event.preventDefault();
        }
    });
}