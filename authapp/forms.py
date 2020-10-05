from django.contrib.auth import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authapp.models import Buyer


class BuyerLoginForm(AuthenticationForm):
    class Meta:
        model = Buyer
        fields = ('username', 'password')
# ++++ для стандартной формы login  из джанго ++++
# перебираем по полям формы и присваиваем класс (бутстраповский)
# def __init__(self, *args, **kwargs):
#     super(BuyerLoginForm, self).__init__(*args, **kwargs)
#     for field_name, field in self.fields.items():
#         field.widget.attrs['class'] = 'form-control'


class BuyerRegistyForm(UserCreationForm):
    class Meta:
        model = Buyer
        fields = ('username', 'first_name', 'last_name', 'age', 'email', 'avatar', 'password1', 'password2')

    # ++++ для стандартной формы login  из джанго ++++
    #     def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)
    #         for field_name, field in self.fields.items():
    #             field.widget.attrs['class'] = 'form-control'
    #             field.help_text = ''

#  +++ без этой функции при сохранении данных регистрации в базу, перманентно ошибка: {'password_mismatch': 'Два поля с паролями не совпадают.'}
    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.set_password(self.cleaned_data['password1'])
        user.save()


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
