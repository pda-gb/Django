from django.contrib import auth
# from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from authapp.forms import BuyerLoginForm, BuyerRegistyForm, BuyerEditForm


def login(request):
    title = 'Вход'
    # создание формы login на основе стандартной из django
    login_form = BuyerLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        # username = request.POST['username'] так мы доверяем полученным данным
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    variable_date = {
        'title': title,
        'login_form': login_form
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
    # print('=============')
    # print(BuyerRegistyForm.error_messages)
    # print('=============')
    variable_date = {
        'title': title,
        'registry_form': registry_form
    }
    return render(request, 'authapp/registry.html', variable_date)


def edit(request):
    title = 'Редактирование'

    if request.method == 'POST':
        edit_form = BuyerEditForm(request.POST, request.FILES, instance=request.user)
        # print(edit_form)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        edit_form = BuyerEditForm(instance=request.user)
    #     print(edit_form)
    # print(edit_form.is_valid())
    variable_date = {
        'title': title,
        'edit_form': edit_form
    }

    return render(request, 'authapp/edit.html', variable_date)
