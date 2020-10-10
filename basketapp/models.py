from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):
    # используем свою модель покупателя указанную в нстройках AUTH_USER_MODEL, а не стандартную джанго
    # related_name='basket_of_buyer' - чот бы ссылаться на корзину
    # из модели покупателя(basket = request.buyer.basket_of_buyer.all())
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket_of_buyer')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)
