'use strict';

let TRAIN_URL = '/pas/member/train/';
let MEMBER_API = '/pas/api/member/';
let VIDEO_TIME = 5;

$(document).ready(function () {
    $('#members-info').click();

    $('#start_get_video_train').on('click', function () {

        let self = this;

        // capture camera and/or microphone
        navigator.mediaDevices.getUserMedia({
            video: true,
            audio: true
        }).then(function (camera) {
            let video_train_element = $('#your-video-id')[0];

            // preview camera during recording
            video_train_element.muted = true;
            video_train_element.srcObject = camera;

            // recording configuration/hints/parameters
            let recordingHints = {
                type: 'video'
            };

            // initiating the recorder
            let recorder = RecordRTC(camera, recordingHints);

            // starting recording here
            recorder.startRecording();

            // auto stop recording after 5 seconds
            let milliSeconds = VIDEO_TIME * 1000;
            setTimeout(function () {

                // stop recording
                recorder.stopRecording(function () {
                    // get recorded blob
                    let blob = recorder.getBlob();

                    let id = $(self).data()['id'];
                    let fileName = $(self).data()['name'] + ".webm";
                    let fileObject = new File([blob], fileName, {
                        type: 'video/webm'
                    });

                    let formData = new FormData();

                    formData.append('id', id);

                    // recorded data
                    formData.append('video-train', fileObject);

                    // file name
                    formData.append('video-filename', fileObject.name);

                    console.log("Video size upload: " + bytesToSize(fileObject.size));

                    // upload using jQuery
                    $.ajax({
                        url: '/api/upload_video/', // replace with your own server URL
                        data: formData,
                        cache: false,
                        contentType: false,
                        processData: false,
                        type: 'POST',
                        success: function (response) {
                            if (response === 'success') {
                                console.log('ok');
                            } else {
                                alert(response); // error/failure
                            }
                        }
                    });

                    // open recorded blob in a new window
                    window.open(URL.createObjectURL(blob));

                    // release camera
                    video_train_element.srcObject = null;
                    camera.getTracks().forEach(function (track) {
                        track.stop();
                    });

                    // you can preview recorded data on this page as well
                    video_train_element.src = URL.createObjectURL(blob);

                });

            }, milliSeconds);
        });
    });


    let btn_train = $('#btn_train');

    btn_train.on('click', function () {
        btn_train.button('loading');
        let member_id = $(this).data()['id'];
        let self = this;
        $.ajax({
            type: "get",
            url: TRAIN_URL,
            data: {id: member_id, isTrain: true},
            success: function (data, text) {
                if (data.status === 'success') {
                    toastr.success(data.message, 'Success');
                    $(self).button('disable');
                    // btn_train.button('reset').attr('disabled', 'disabled');
                    $('#btn_train').button('reset');
                    $('#member_train_warning').html('Done!').css('color', 'green');
                    $('#member_threshold').html(data.threshold);
                } else if (data.status === 'warning') {
                    toastr.warning(data.message, 'Warning');
                    $(self).button('reset').attr('disabled', 'disabled');
                } else {
                    toastr.error('Cannot train!', 'Fail');
                    $(self).button('reset').removeAttr('disabled');
                }
            },
            error: function (request, status, error) {
                console.log(error);
                toastr.error(error, 'Fail');
                $(self).button('reset').removeAttr('disabled');
            }
        });
    });

    $('#btn_get_more_calculate_money').on('click', function () {
        let member_id = $(this).data()['id'];
        $.ajax({
            type: "get",
            url: '/pas/calculate_hour/',
            data: {id: member_id},
            success: function (data, text) {
                if (data.status === 'success') {
                    toastr.success(data.message, 'Success');
                    console.log(data);
                }
            },
            error: function (request, status, error) {
                console.log(error);
            }
        });
    });

    $('#btn_change_avatar').on('click', function () {
        $(this).css('display', 'none');
        $('.change_avatar_container').css('display', '');
    });

    $('#upload_avatar').change(function (e) {
        let self = $(this);

        let img_url = URL.createObjectURL(e.target.files[0]);
        $('#img_member_avatar').attr('src', img_url);
        let img = e.target.files[0];
        let data = new FormData();
        data.append('type', 'upload_avatar');
        data.append('id', self.data()['id']);
        data.append('img', img);

        console.log(img);
        $.ajax({
            type: "post",
            contentType: false,
            processData: false,
            url: MEMBER_API,
            data: data,
            success: function (data, text) {
                $('.change_avatar_container').css('display', 'none');
                $('#btn_change_avatar').css('display', '');
                toastr.success(data.message, 'Success');
            },
            error: function (request, status, error) {
                console.log(error);
            }
        });
    });

    $('#btn_cancel_change_avatar').on('click', function () {
        $('.change_avatar_container').css('display', 'none');
        $('#btn_change_avatar').css('display', '');
    })

});