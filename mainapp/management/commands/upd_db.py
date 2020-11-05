# создание быстрых команд для выполнения частых задач ($: python manage.py make_fill_db )
# если из json файла в базу добавляется в поле с  UNIQUE=True уже имеющееся значение, то будет ошибка

from django.core.management import BaseCommand

from authapp.models import Buyer, BuyerProfile

# связываем всех сущ. пользователей с новой моделью
class Command(BaseCommand):  # свой класс унаследуем от BaseCommand
    def handle(self, *args, **options):  # с обязательным методом handle
        buyers = Buyer.objects.all()
        for buyer in buyers:
            buyer_profile = BuyerProfile.objects.create(buyer=buyer)
            buyer_profile.save()
