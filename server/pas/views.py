import os, uuid, datetime, pytz, shutil
from django.utils import timezone, dateparse
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.files.images import ImageFile, File
from django.core.files.storage import default_storage
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .member_forms import AddMemberForm
from .models import Member, Logs

from . import get_faces_to_train, face_train, face_recognize, const, \
    mqtt

from server import settings


def index(request):
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    logs_for_today = Logs.objects.filter(time_stamp__range=(today_min, today_max))
    context = {
        'logs': logs_for_today
    }
    return render(request, 'pas/index.html', context)


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/')


def login_view(request):
    # logout(request)
    # Redirect to a success page.
    return render(request, 'pas/login.html')


@login_required(login_url='/admin/login/')
def devices_info(request):
    return render(request, 'pas/404_error.html')


@login_required(login_url='/admin/login/')
def warning(request):
    if request.method == 'POST':
        id = request.POST['id']
        # request.POST['time_stamp'] = "2018-04-17 23:04:34"
        time_stamp = dateparse.parse_datetime(request.POST['time_stamp'])
        tz = pytz.timezone(settings.TIME_ZONE).localize(time_stamp)
        log = Logs.objects.get(member_id=id, time_stamp=tz)
        log.image.delete(save=True)
        log.delete()

        http_response = {
            'status': 'success',
            'message': 'Verify member success!',
        }
        return JsonResponse(http_response)
    logs_warning = Logs.objects.filter(result_auth=False).all()

    # api to get number of warning to display on side bar
    if request.GET['is_get_all']:
        http_response = {
            'status': 'success',
            'data': len(logs_warning),
        }
        return JsonResponse(http_response)
    context = {
        'logs_warning': logs_warning
    }
    return render(request, 'pas/warning.html', context)


@login_required(login_url='/admin/login/')
def members_info(request):
    if request.method == 'POST':
        post_data = request.POST
        # edit or delete member
        if 'id' in post_data:
            if post_data['action'] == 'delete':
                member_id = post_data['id']
                member = Member.objects.get(id=member_id)
                logs = Logs.objects.filter(member_id=member_id)
                if len(logs):
                    for log in logs:
                        log.image.delete(save=True)
                        log.delete()
                # member.avatar.delete(save=True)

                label = member.recognize_label
                # delete train and test images
                faces_train_path = os.path.join(const.FACE_TRAIN_FOLDER, str(label))
                if os.path.isdir(faces_train_path):
                    shutil.rmtree(faces_train_path)

                # delete file model .yml
                eigenface_model_path = os.path.join(const.EIGENFACES_FOLDER, str(label) + ".yml")
                if os.path.isfile(eigenface_model_path):
                    os.remove(eigenface_model_path)

                member.delete()

                http_response = {
                    'status': 'success',
                    'message': 'Delete member success!',
                }
                return JsonResponse(http_response)
            elif post_data['action'] == 'edit':
                pass
        # add member
        else:
            # create a form instance and populate it with data from the request:
            form = AddMemberForm(request.POST)
            member_uuid = uuid.uuid4()
            # check whether it's valid:
            if form.is_valid():
                u = Member(
                    id=member_uuid,
                    name=form.data['name'],
                    email=form.data['email'],
                    card_id=form.data['card_id'],
                    course=form.data['course'],
                    research_about=form.data['research_about']
                )
                u.save()
                messages.success(request, 'Add member success!')
                return redirect(request.path)

    form = AddMemberForm
    try:
        member_list = Member.objects.all()
        context = {
            'member_list': member_list,
            'form': form,
        }
    except Member.DoesNotExist:
        raise Http404("Member table does not exist")
    return render(request, 'pas/member/index.html', context)


def members_api(request):
    try:
        member_list = Member.objects.all()
    except Member.DoesNotExist:
        raise Http404("Member table does not exist")
    return HttpResponse(member_list)


def server_authentication(request):
    if request.method == 'POST':
        card_id = request.POST['card_id']
        member = Member.objects.get(card_id=card_id)
        last_iamge_name = ''
        # save images to /tmp folder
        for face_key in request.FILES:
            last_iamge_name = face_key
            data = request.FILES[face_key]
            face = ImageFile(data)
            face_path = 'tmp/' + str(data)
            if default_storage.exists(face_path):
                default_storage.delete(face_path)
            default_storage.save(face_path, face)

        # get result of predict list images
        list_predicts = face_recognize.recognition(member.recognize_label)
        if len(list_predicts):
            last_iamge_name = list_predicts[0][0]

        # check threshold
        result_auth = False
        f_name = None
        for file_name, conf in list_predicts:
            if conf < member.threshold:
                result_auth = True
                f_name = file_name
                break
        # publish result auth to mqtt topic /pas/mqtt/icse/auth
        mqtt.publish(result_auth)

        # get latest logs to check user in or out
        try:
            last_log = Logs.objects.filter(member_id=member.id).latest('time_stamp')
            is_go_in = False if last_log.is_go_in else True
        except Logs.DoesNotExist:
            is_go_in = True

        # save logs
        log = Logs(
            time_stamp=timezone.now(),
            member=member,
            result_auth=result_auth,
            is_go_in=is_go_in,
        )
        f_name = f_name if result_auth else last_iamge_name
        file_path = os.path.join(const.TMP_FOLDER, f_name)
        file_data = File(open(file_path, 'rb'))
        log.image.save(f_name, file_data, save=True)
        log.save()

        return HttpResponse("POST request success")
    return HttpResponse("Upload image success")


@login_required(login_url='/admin/login/')
def member_profile(request):
    member_id = request.GET['id']
    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        raise Http404("Member does not exist")
    label = member.recognize_label
    label_path = const.FACE_TRAIN_FOLDER + str(label) + "/"
    normal_faces = os.path.exists(label_path + const.NORMAL_FACES_FOLDER_NAME)
    smile_faces = os.path.exists(label_path + const.SMILE_FACES_FOLDER_NAME)
    closed_eye_faces = os.path.exists(label_path + const.CLOSED_EYE_FACES_FOLDER_NAME)
    no_glass_faces = os.path.exists(label_path + const.NO_GLASS_FACES_FOLDER_NAME)
    test_faces = os.path.exists(label_path + const.TEST_FACES_FOLDER_NAME)
    context = {
        'member': member,
        const.NORMAL_FACES_FOLDER_NAME: normal_faces,
        const.SMILE_FACES_FOLDER_NAME: smile_faces,
        const.CLOSED_EYE_FACES_FOLDER_NAME: closed_eye_faces,
        const.NO_GLASS_FACES_FOLDER_NAME: no_glass_faces,
        const.TEST_FACES_FOLDER_NAME: test_faces
    }
    return render(request, 'pas/member/profile.html', context)


@login_required(login_url='/admin/login/')
def train_face(request):
    member_id = request.GET['id']
    member = Member.objects.get(id=member_id)
    isTrain = request.GET['isTrain']
    if isTrain and isTrain == "true":
        if not member.is_train:
            label = member.recognize_label
            images_trained = face_train.train(label)
            get_threshold = face_recognize.get_threshold(label)
            threshold = int(get_threshold[0])
            member.is_train = True
            member.threshold = threshold
            member.save()
            http_response = {
                'status': 'success',
                'message': 'Training success with {0} images -- '
                           'Get threshold success with {1} images'.format(images_trained, get_threshold[1]),
                'threshold': threshold,
            }

        else:
            http_response = {
                'status': 'warning',
                'message': 'This member was had file train!'
            }
    else:
        member_label = member.recognize_label
        face_type = request.GET['type']
        get_faces_to_train.main(member_label, face_type)
        http_response = {
            'status': 'success',
            'message': 'Have taken enough 50 faces image!'
        }
    return JsonResponse(http_response)
