from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from cafeapp.models import Cafe


class BannerImage(models.Model):
    image = ProcessedImageField(upload_to='images/', processors=[ResizeToFill(1100, 200)], format='JPEG', options = {'quality': 90})
    cafe = models.ForeignKey(Cafe, on_delete=models.SET_NULL, related_name='banners', null=True, blank=True)

# class WelcomeImage(models.Model):
#     welcome_img = ProcessedImageField(upload_to='images/', processors=[ResizeToFill(890, 300)], format='JPEG', options = {'quality': 90})
