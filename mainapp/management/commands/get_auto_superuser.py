from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from authapp.models import Buyer


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = get_user_model()
        user.objects.create_superuser(username='django', email='django@geekshop', password='geekbrains', age='1987-12-31')
