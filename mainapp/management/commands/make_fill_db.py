# создание быстрых команд для выполнения частых задач ($: python manage.py make_fill_db.py )
import json
import os

from django.conf import settings
from django.core.management import BaseCommand

from mainapp.models import ProductCategory, Product

path_json = os.path.join(settings.BASE_DIR, 'json')  # путь к json папке


def load_from_json(file_name):
    """

    :param file_name: имя необходимого json файла
    :return: выводит содержимое
    """
    with open(os.path.join(path_json, file_name + '.json')) as file_json:
        return json.load(file_json)


class Command(BaseCommand):  # свой класс унаследуем от BaseCommand
    def handle(self, *args, **options):  # с обязательным методом handle
        categories = load_from_json("categories")
        for itm in categories:
            ProductCategory.objects.create(**itm)  # распаковка словаря соответственно модели и распред. по ключам с
                                                   # одновременным сохр. в базу( .save() )

        products = load_from_json("products")
        for itm in products:
            # т.к. в products категория просто сторока, а в таблице связанное поле, то находим и присваиваем его
            category_name = ProductCategory.objects.get(name=itm["category"])
            itm["category"] = category_name
            Product.objects.create(**itm)

            # types = load_from_json("types")
        # for itm in types:
        #     ProductType.objects.create(**itm)
