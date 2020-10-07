# создание быстрых команд для выполнения частых задач ($: python manage.py make_fill_db )
# если из json файла в базу добавляется в поле с  UNIQUE=True уже имеющееся значение, то будет ошибка
import json
import os

from django.conf import settings
from django.core.management import BaseCommand

from mainapp.models import ProductCategory, Product, ProductType

path_json = os.path.join(settings.BASE_DIR, 'json')  # путь к json папке


def load_from_json(file_name):
    """

    :param file_name: имя необходимого json файла
    :return: выводит содержимое
    """
    with open(os.path.join(path_json, file_name + '.json'), 'r', encoding='utf-8') as file_json:
        return json.load(file_json)


class Command(BaseCommand):  # свой класс унаследуем от BaseCommand
    def handle(self, *args, **options):  # с обязательным методом handle

        # categories = load_from_json("categories")
        # for itm in categories:
        #     ProductCategory.objects.create(**itm)  # распаковка словаря соответственно модели и распред. по ключам с
        #     # одновременным сохр. в базу( .save() )
        #
        # pr_types = load_from_json("types")
        # for itm in pr_types:
        #     ProductType.objects.create(**itm)

        products = load_from_json("products")
        for itm in products:
            # т.к. в products категория просто сторока, а в таблице связанное поле, то находим и присваиваем его
            category_name = ProductCategory.objects.get(name=itm["category"])
            type_name = ProductType.objects.get(name=itm["type"])
            itm["type"] = type_name
            itm["category"] = category_name
            Product.objects.create(**itm)
