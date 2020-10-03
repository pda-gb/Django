from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import BuyerLoginForm


def login(request):
    title = 'Вход'
    login_form = BuyerLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        # username = request.POST['username'] так мы доверяем полученным данным
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
        variable_date = {
            'title': title,
            'login_form': login_form
        }
        return (request, variable_date)


def logout(request):
    pass
