'use strict';

let TRAIN_URL = '/pas/member/train';

$(document).ready(function () {
    $('#members-info').click();

    $('#btn_get_face1').on('click', function () {
        $(this).attr('disabled', 'disabled');
        let member_email = $(this).data()['email'];
        $.ajax({
            type: "get",
            url: TRAIN_URL,
            data: {email: member_email, isTrain: false},
            success: function (data, text) {
                console.log(data);
                if(data === 'success' || data === 'Success'){
                    toastr.success('Have taken enough 50 faces image!', 'Success');
                    $('#member_train_warning').html('Have taken enough 50 faces image. Let train now!');
                    $('#btn_train').removeAttr('disabled');
                } else {
                    toastr.success('Cannot take face images!', 'Fail');
                    $(this).removeAttr('disabled');
                    $('#btn_train').attr('disabled', 'disabled');
                }
            },
            error: function (request, status, error) {
                console.log(error);
            }
        });
    })

    $('#btn_train').on('click', function () {
        $(this).attr('disabled', 'disabled');
        let member_email = $(this).data()['email'];
        $.ajax({
            type: "get",
            url: TRAIN_URL,
            data: {email: member_email, isTrain: true},
            success: function (data, text) {
                console.log(data);
                if(data === 'success' || data === 'Success'){
                    toastr.success('Training success!', 'Success');
                    $(this).attr('disabled', 'disabled');
                    $('#member_train_warning').html('Done!').css('color', 'green');
                } else {
                    toastr.success('Cannot take face images!', 'Fail');
                    $(this).removeAttr('disabled');
                }
            },
            error: function (request, status, error) {
                console.log(error);
            }
        });
    });
});