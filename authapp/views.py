from django.conf import settings
from django.contrib import auth
from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from authapp.forms import BuyerLoginForm, BuyerRegistyForm, BuyerEditForm, BuyerProfileEditForm
from authapp.models import Buyer
from basketapp.models import Basket


def verification(request, email, activation_key):
    try:  # если user не существует
        user = Buyer.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activations_expired():
            user.is_active = True
            user.save()
            # укажем явно backend для login, т.к. их тереь есть от соц. сетей
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'authapp/verification.html')
        else:
            print('++++++++')
            print(f'error activation of: {email}')
            return render(request, 'authapp/verification.html')
    except Exception as e:
        print('====fail activation====')
        print(e.args)
        return HttpResponseRedirect(reverse('main'))


def send_verifications_email(user):
    verify_link = reverse('authapp:verification', args=[user.email, user.activation_key])
    subject = f'Подтверждение регистрации {user.username}'
    message = f'Для подтверждения регистрации перейдите по ссылке: \n {settings.DOMAIN_NAME}{verify_link}'
    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def login(request):
    title = 'Вход'
    # создание формы login на основе стандартной из django
    login_form = BuyerLoginForm(data=request.POST)
    # защита от незарегистрир. пользователя
    _next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():
        # username = request.POST['username'] так мы доверяем полученным данным
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            return HttpResponseRedirect(reverse('main'))

    # Если пришли из формы регистрации, получаем True
    from_registry = request.session.get('is_registry', None)
    if from_registry:  # сразу очищаем сессию, что бы заново не получать уведом. при входе в login
        del request.session['is_registry']

    variable_date = {
        'title': title,
        'login_form': login_form,
        'next': _next,
        'from_registry': from_registry,
    }

    return render(request, 'authapp/login.html', variable_date)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def registry(request):
    title = 'Регистрация'
    if request.method == 'POST':
        registry_form = BuyerRegistyForm(request.POST, request.FILES)
        if registry_form.is_valid():
            user = registry_form.save()
            if send_verifications_email(user):
                print('===verification success===')
                request.session['is_registry'] = True
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                print('===verification error===')
                request.session['is_registry'] = False
                return HttpResponseRedirect(reverse('auth:login'))
    else:
        registry_form = BuyerRegistyForm()
    variable_date = {
        'title': title,
        'registry_form': registry_form
    }
    return render(request, 'authapp/registry.html', variable_date)

# (вар.1) все операции контроллера одна атомарная транзакция, т.к. edit_form
# и profile_form связаны через сигнал в модели
@transaction.atomic()
def edit(request):
    title = 'Редактирование'

    shop_user = request.user  # узнаём кто зашёл, если зареган, выводим количество товаров у "корзинки"
    basket_itm = None
    if not shop_user.is_anonymous:
        basket_itm = Basket.objects.filter(buyer=request.user)  # собираем товары из корзины, для отображ. кол.-ва

    if request.method == 'POST':
        edit_form = BuyerEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = BuyerProfileEditForm(request.POST, instance=request.user.buyerprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            # (вар.2) с пом. контекстного менеджера  атомарны только нужные операции
            # with transaction.atomic():
            edit_form.save()  # по сигналу(receiver) в модели сохранится profile_form
            return HttpResponseRedirect(reverse('main'))
    else:
        edit_form = BuyerEditForm(instance=request.user)
        profile_form = BuyerProfileEditForm(instance=request.user.buyerprofile)

    variable_date = {
        'title': title,
        'edit_form': edit_form,
        'basket_itm': basket_itm,
        'profile_form': profile_form
    }

    return render(request, 'authapp/edit.html', variable_date)
