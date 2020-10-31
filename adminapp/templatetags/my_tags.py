from django import template
from django.conf import settings

register = template.Library()


def media_folder_product(path_string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам продуктов
    products_images/product1.jpg --> /media/products_images/product1.jpg
    """
    if not path_string:
        path_string = 'foto_product/default.png'
    return f'{settings.MEDIA_URL}{path_string}'


# первый способ регистрирования шаблона
register.filter('foto_product', media_folder_product)


# второй способ регистрирования шаблона
@register.filter(name='foto_user')
def media_folder_user(path_string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам пользователей
    users_avatars/user1.jpg --> /media/users_avatars/user1.jpg
    """
    if not path_string:
        path_string = 'users_avatar/default.png'
    return f'{settings.MEDIA_URL}{path_string}'
