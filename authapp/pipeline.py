from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlunparse, urlencode

import requests
from social_core.exceptions import AuthForbidden

from authapp.models import BuyerProfile, Buyer


def save_buyer_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse(('https', 'api.vk.com', '/method/users.get', None,
                          urlencode(OrderedDict(fields='.'.join(('bdate', 'sex',
                                                                 'about', 'foto'
                                                                 )),
                                                access_token=
                                                response['access_token'],
                                                v='5.92')),
                          None
                          ))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]

    # если аккаунт не закрыт или не закрыт доступ запрашивающему
    if not data['can_access_closed'] or not data['can_access_closed']:
        if data['sex']:
            if data['sex'] == 0:  # пол не указан
                pass
            if data['sex'] == 1:
                user.shopuserprofile.gender = BuyerProfile.FEMALE
            if data['sex'] == 2:
                user.shopuserprofile.gender = BuyerProfile.MALE

        if data['about']:
            user.shopuserprofile.aboutMe = data['about']

        if data['bdate']:
            bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

            from django.utils import timezone

            age = timezone.now().date().year - bdate.year
            if age < 18:
                user.delete()
                # при DEBUG = True выдаст ошибку, иначе на LOGIN_ERROR_URL
                raise AuthForbidden('social_core.backends.vk.VKOAuth2')
            user.save()

        if data['foto']:
            path_avatar = data['foto']
            Buyer.avatar = f'/users_avatar/{path_avatar}'

