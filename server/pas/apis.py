import datetime
from django.http import Http404, HttpResponse, JsonResponse
from django.utils.timezone import now, localtime

from .models import Member, Logs, Money


def get_warning_number(request):
    pass


def calculate_hour(request):
    member_id = request.GET['id']
    member = Member.objects.get(id=member_id)
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    logs_for_today = Logs.objects.filter(time_stamp__range=(today_min, today_max),
                                         member_id=member_id)
    total_hour = None
    is_go_in = True
    if len(logs_for_today):
        for log in logs_for_today:
            if log.is_go_in:
                start_time = log.time_stamp
            else:
                if total_hour:
                    total_hour += log.time_stamp - start_time
                else:
                    total_hour = log.time_stamp - start_time
                start_time = None
    hour_convert = divmod(total_hour.days * 86400 + total_hour.seconds, 60)

    local_today = localtime(now()).date()
    money = Money(member=member,total_hour=hour_convert[0],date=local_today)
    money.save()

    return JsonResponse({'ok': 'ok'})