import json
import os
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

path_json = os.path.join(settings.BASE_DIR, 'json')  # путь к json папке


def load_from_json(file_name):
    """

    :param file_name: имя необходимого json файла
    :return: выводит содержимое
    """
    with open(os.path.join(path_json, file_name + '.json'), 'r', encoding='utf-8') as file_json:
        return json.load(file_json)


class Command(BaseCommand):
    def handle(self, *args, **options):
        secret_value = load_from_json("secret")
        user = get_user_model()
        user.objects.create_superuser(username=secret_value["SU_name"], email=secret_value["SU_email"],
                                      password=secret_value["SU_password"],
                                      age=secret_value["SU_age"])
