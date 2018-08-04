from django.db import models
from django.utils import timezone
import datetime
import os
import mysite.settings as settings


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class ProfileImage(models.Model):
    name = models.CharField(max_length=100)
    file = models.ImageField(settings.MEDIA_ROOT)

    def url(self):
        # returns a URL for either internal stored or external image url
        if self.externalURL:
            return self.externalURL
        else:
            # is this the best way to do this??
            return os.path.join('/', settings.MEDIA_URL, os.path.basename(str(self.image)))

    def __str__(self):
        return "{}".format(self.name)