from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from authapp.models import Buyer


class BuyerLoginForm(AuthenticationForm):
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
    class Meta:
        model = Buyer
        fields = ('username', 'first_name', 'last_name', 'age', 'email', 'avatar', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


# переделать, так как вводится не возраст, а дата

#     def clean_age(self):
#         """
#         доп валидация по возрасту
#         :return:
#         """
#         data = self.cleaned_data['age']
#         if data < 18:
#             raise forms.ValidationError("Вы слишком молоды!")
#         return data


class BuyerEditForm(UserChangeForm):
    class Meta:
        model = Buyer
        fields = ('username', 'first_name', 'last_name', 'age', 'email', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

# переделать, так как вводится не возраст, а дата

# def clean_age(self):
#     data = self.cleaned_data['age']
#     if data < 18:
#         raise forms.ValidationError("Вы слишком молоды!")
#
#     return data
