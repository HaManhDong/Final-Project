from django.db import models


class User(models.Model):
    name = models.TextField('user name')
    email = models.EmailField(primary_key=True)
    card_id = models.TextField('card id')

    def __str__(self):
        return self.name


class Logs(models.Model):
    time_stamp = models.DateTimeField('Time user in/out', primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    value = models.IntegerField('0/1 - out/in')

    # def __str__(self):
    #     return self.time_stamp

