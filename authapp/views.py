from django.contrib import auth
# from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from authapp.forms import BuyerLoginForm, BuyerRegistyForm, BuyerEditForm
from basketapp.models import Basket


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
    variable_date = {
        'title': title,
        'login_form': login_form,
        'next': _next
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
            registry_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        registry_form = BuyerRegistyForm()
    variable_date = {
        'title': title,
        'registry_form': registry_form
    }
    return render(request, 'authapp/registry.html', variable_date)


def edit(request):
    title = 'Редактирование'

    shop_user = request.user  # узнаём кто зашёл, если зареган, выводим количество товаров у "корзинки"
    basket_itm = None
    if not shop_user.is_anonymous:
        basket_itm = Basket.objects.filter(buyer=request.user)  # собираем товары из корзины, для отображ. кол.-ва

    if request.method == 'POST':
        edit_form = BuyerEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        edit_form = BuyerEditForm(instance=request.user)

    variable_date = {
        'title': title,
        'edit_form': edit_form,
        'basket_itm': basket_itm
    }

    return render(request, 'authapp/edit.html', variable_date)
