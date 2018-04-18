'use strict';

$(document).ready(function () {

    let WARNING_API = '/pas/warning/';

    $('#warning').click();

    $('#pas_datatables_warning').DataTable({
        "drawCallback": function (settings) {
            $('.btn_verify_member').on('click', function () {
                let user_id = $(this).data()['id'];
                let time_stamp = $(this).data()['time_stamp'];
                $.post(WARNING_API, {id: user_id, time_stamp: time_stamp})
                    .done(function (data) {
                        if (data.status === 'success') {
                            toastr.success(data.message, 'Success');
                        }
                        $('#modal-delete-user').modal('toggle');
                    })
                    .fail(function (err) {
                        console.log(err);
                        $('#modal-delete-user').modal('toggle');
                        toastr.error("Have some error when delete this member!", "Fail");
                    })
            });
        }
    });

});

