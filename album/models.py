from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to='media/photos')
    creation_date = models.DateTimeField(auto_now_add=True)
    fav = models.ManyToManyField(User, related_name='fav')


