import hashlib
import random

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from authapp.models import Buyer, BuyerProfile


class BuyerLoginForm(AuthenticationForm):

    error_css_class = 'text-danger'  # подсвечиваем красным поля с ошибкой

    class Meta:
        model = Buyer
        fields = ('username', 'password')

    # перебираем по полям формы и присваиваем класс
    def __init__(self, *args, **kwargs):
        super(BuyerLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class BuyerRegistyForm(UserCreationForm):

    error_css_class = 'text-danger'  # подсвечиваем красным поля с ошибкой

    class Meta:
        model = Buyer
        fields = ('username', 'first_name', 'last_name', 'age', 'email', 'avatar', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(BuyerRegistyForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    # переопределяем метод сохранения
    def save(self, **kwargs):
        # берём пользователя из родит. класса UserCreationForm
        user = super(BuyerRegistyForm, self).save()
        user.is_active = False  # теперь изначально неактивен
        # создаём ключ на основе соли и почты
        salt = hashlib.sha256(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha256((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user

    def clean_age(self):
        """
        доп валидация по возрасту
        :return:
        """
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data


class BuyerEditForm(UserChangeForm):

    error_css_class = 'text-danger'  # подсвечиваем красным поля с ошибкой

    class Meta:
        model = Buyer
        fields = ('username', 'first_name', 'last_name', 'age', 'email', 'avatar')

    def __init__(self, *args, **kwargs):
        super(BuyerEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data


class BuyerProfileEditForm(forms.ModelForm ):

    error_css_class = 'text-danger'  # подсвечиваем красным поля с ошибкой

    class Meta:
        model = BuyerProfile
        fields = ('tagline', 'about_me', 'gender')

    def __init__(self, *args, **kwargs):
        super(BuyerProfileEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
