from django.contrib.auth.forms import AuthenticationForm

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
