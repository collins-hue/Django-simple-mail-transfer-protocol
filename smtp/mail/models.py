from django.db import models

from django.urls import reverse


class Subscriber(models.Model):
    email = models.EmailField(null=False, unique=True, default='myemail@mail.com', blank=False)

