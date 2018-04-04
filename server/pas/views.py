from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.core.files.images import ImageFile
from django.core.files.storage import default_storage
from django.contrib import messages

from .member_forms import AddMemberForm

from .models import Member

from . import get_faces_to_train, face_train


def index(request):
    return render(request, 'pas/index.html')


def devices_info(request):
    return render(request, 'pas/devices.html')


def members_info(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddMemberForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            u = Member(
                name=form.data['name'],
                email=form.data['email'],
                card_id=form.data['card_id'],
                course=form.data['course'],
                research_about=form.data['research_about']
            )
            u.save()
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
    # messages.success(request, 'Add memeber success!')
    return render(request, 'pas/member/index.html', context)


def members_api(request):
    try:
        member_list = Member.objects.all()
    except Member.DoesNotExist:
        raise Http404("Member table does not exist")
    return HttpResponse(member_list)


def upload_images(request):
    if request.method == 'POST':
        card_id = request.POST['card_id']
        member = Member.objects.get(card_id=card_id)
        for face_key in request.FILES:
            data = request.FILES[face_key]
            face = ImageFile(data)
            face_path = 'tmp/' + str(data)
            if default_storage.exists(face_path):
                default_storage.delete(face_path)
            default_storage.save(face_path, face)

        return HttpResponse("POST request success")
    return HttpResponse("Upload image success")


def member_profile(request):
    member_email = request.GET['email']
    try:
        member = Member.objects.get(email=member_email)
    except Member.DoesNotExist:
        raise Http404("Member does not exist")
    context = {'member': member}
    return render(request, 'pas/member/profile.html', context)


def train_face(request):
    member_email = request.GET['email']
    member = Member.objects.get(email=member_email)
    isTrain = request.GET['isTrain']
    if isTrain and isTrain == "true" and not member.is_train:
        face_train.train(member.recognize_label)
        member.is_train = True
        member.save()
    else:
        member_label = member.recognize_label
        get_faces_to_train.main(member_label)
    return HttpResponse('success')

