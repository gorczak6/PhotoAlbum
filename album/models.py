from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    user = models.ForeignKey(User)
    photo = models.FileField
