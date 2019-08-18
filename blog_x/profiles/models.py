from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    date_of_birth = models.DateField(verbose_name='dob', auto_now=False, blank=True)

    def __str__(self):
        return self.user.username
