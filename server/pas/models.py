from django.db import models


class Member(models.Model):
    name = models.TextField('member name')
    email = models.EmailField()
    card_id = models.TextField('card id')
    course = models.TextField('course', null=True)
    registered_day = models.DateField(auto_now_add=True)
    latest_image = models.ImageField(null=True)
    avatar = models.ImageField(null=True)
    recognize_label = models.AutoField(primary_key=True)
    research_about = models.TextField('research', null=True)
    is_train = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Logs(models.Model):
    time_stamp = models.DateTimeField('Time member in/out', primary_key=True)
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    value = models.IntegerField('0/1 - out/in')

    # def __str__(self):
    #     return self.time_stamp

