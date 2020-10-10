from django.contrib.auth.models import AbstractUser
from django.db import models


class Buyer(AbstractUser):
    # blank  сделать картинку "нет фото"
    avatar = models.ImageField(verbose_name='Фото', upload_to='users_avatar', blank=True)
    # age = models.PositiveSmallIntegerField(verbose_name='Ваш возраст')
    age = models.DateField(verbose_name='Ваша дата рождения')
