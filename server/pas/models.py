import uuid
from django.db import models


class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField('member name')
    email = models.EmailField()
    card_id = models.TextField('card id')
    course = models.TextField('course', null=True)
    registered_day = models.DateField(auto_now_add=True)
    avatar = models.ImageField(null=True, upload_to='avatar')
    research_about = models.TextField('research', null=True)
    is_train = models.BooleanField(default=False)
    threshold = models.IntegerField(null=True)

    # This is what you would increment on save
    # Default this to one as a starting point
    recognize_label = models.IntegerField(default=1)

    # Rest of your model data

    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            last_id = Member.objects.all().aggregate(largest=models.Max('recognize_label'))['largest']

            # aggregate can return None! Check it first.
                # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_id is not None:
                self.recognize_label = last_id + 1

        super(Member, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Logs(models.Model):
    time_stamp = models.DateTimeField('Time member in/out', primary_key=True)
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    is_go_in = models.BooleanField(null=False)
    result_auth = models.BooleanField(null=False)
    image = models.ImageField(upload_to='logs/%Y/%m/%d')

    # def __str__(self):
    #     return self.time_stamp


class Money(models.Model):
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    total_hour = models.IntegerField('Hour per day', null=False)
    date = models.DateField(null=False)