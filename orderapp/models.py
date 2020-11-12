from django.conf import settings
from django.db import models

from mainapp.models import Product

""" 
(!) created updated is_active  - данные поля создавать во всех моделях, с 
которыми работает пользователь (!)
"""


class Order(models.Model):
    FORMING = 'FM'
    SEND_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    DONE = 'DN'
    CANCEL = 'CNC'
    ORDER_STATUSES = (
        (FORMING, 'формируется'),
        (SEND_TO_PROCEED, 'отправлен в обработку'),
        (PROCEEDED, 'обработан'),
        (PAID, 'оплачен'),
        (READY, 'готов к выдаче'),
        (DONE, 'выдан'),
        (CANCEL, 'отменён'),
    )
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              verbose_name='Покупатель')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.CharField(max_length=3, choices=ORDER_STATUSES,
                              default=FORMING)
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    class Meta:
        # сортировка по умолчанию от более новых к старым заказам:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Текущий  заказ: #{self.id}'

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_product_type_quantity(self):
        items = self.orderitems.select_related()
        return len(items)

    def get_total_cost(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity * x.product.price, items)))

    # переопределяем метод, удаляющий объект...
    def delete(self):
        for item in self.orderitems.select_related():
            # возвращаем кол.-во товара из заказа на склад
            item.product.quantity += item.quantity
            item.product.save()
        self.is_active = False  # ... на неактивный
        self.save()


# аналогично корзине - заказ Order состоит из отдельных заказов OrderItem
# кажого продукта
class OrderItem(models.Model):
    # связываем модель с основной. При удалении основного, данный экзампляр
    # тоже удалится
    order = models.ForeignKey(Order, related_name="orderitems",
                              on_delete=models.CASCADE, verbose_name='позиция')
    product = models.ForeignKey(Product, verbose_name='продукт',
                                on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество',
                                           default=0)

    def get_product_cost(self):
        return self.product.price * self.quantity
