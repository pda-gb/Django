from django.contrib.auth.forms import AuthenticationForm

from authapp.models import Buyer


class BuyerLoginForm(AuthenticationForm):
    class Meta:
        model = Buyer
        fields = ('username', 'password')
