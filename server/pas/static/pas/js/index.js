'use strict';

$(document).ready(function () {
    $('#dashboard').click();

    $.ajax({
        type: "get",
        url: '/pas/warning',
        data: {is_get_all: true},
        success: function (data, text) {
            if (data.status === 'success') {
                $('#box_warning_value').html(data.data);
            } else {
                toastr.error('Cannot get number of warning!', 'Fail');
            }
        },
        error: function (request, status, error) {
            console.log(error);
            toastr.error('Cannot get number of warning!', 'Fail');
        }
    });

});

