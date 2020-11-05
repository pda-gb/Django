from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class Buyer(AbstractUser):
    avatar = models.ImageField(verbose_name='Фото', upload_to='users_avatar', blank=True)
    # age = models.PositiveSmallIntegerField(verbose_name='Ваш возраст')
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)


    # ключ активации и время данное на активацию
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=24)))

    # метод проверки срока годности ключа
    def is_activations_expired(self):
        if now() <= self.activation_key_expires:
            return False
        return True
