from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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


# связь 1 к 1
class BuyerProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )
    buyer = models.OneToOneField(Buyer, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='Теги', max_length=128, blank=True)
    about_me = models.TextField(verbose_name='Обо мне', blank=True)
    gender = models.CharField(verbose_name='Пол', max_length=1, choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=Buyer)
    def create_buyer_profile(sender, instance, created, **kwargs):
        if created:
            BuyerProfile.objects.create(buyer=instance)

    @receiver(post_save, sender=Buyer)
    def save_buyer_profile(sender, instance, **kwargs):
        instance.buyerprofile.save()
