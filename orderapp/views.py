from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from basketapp.models import Basket
from orderapp.forms import OrderItemForm
from orderapp.models import Order, OrderItem


# По умолчанию для ListView Django будет искать шаблон с именем вида:
# «<имя класса>_list.html».
# LoginRequiredMixin - добавляем миксин для доступа только залогиненным юзерам
class OrderList(LoginRequiredMixin, ListView):
    model = Order

    def get_queryset(self):
        """
        Переопределили метод «get_queryset()» для того, чтобы пользователь
        видел только свои заказы
        """
        return Order.objects.filter(buyer=self.request.user)


# Для классов CreateView и UpdateView шаблон должен иметь имя вида
# «<имя класса>_form.html»
class OrderItemsCreate(LoginRequiredMixin, CreateView):
    model = Order
    # в соответствии с моделью все поля, кроме пользователя buyer, создаются
    # автоматически, buyer добавим позже
    fields = []
    success_url = reverse_lazy('orderapp:orders_list')

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)

    # добавляем данные в контекст, пересобираем в одну форму OrderItemForm
    # из Order и OrderItem
    def get_context_data(self, **kwargs):
        context_data = super(OrderItemsCreate, self).get_context_data(**kwargs)
        order_form_set = inlineformset_factory(Order, OrderItem,
                                               form=OrderItemForm, extra=1)
        if self.request.POST:  # если пост запрос, заполняем данными
            formset = order_form_set(self.request.POST)
        else:
            # из корзины собираем все позиции("товары-корзинки") пользователя(!)
            basket_items = Basket.get_items(self.request.user)
            if len(basket_items):  # если в корзине что-то есть
                # создаём форму заказа
                order_form_set = inlineformset_factory(Order, OrderItem,
                                                       form=OrderItemForm,
                                                       extra=len(basket_items))
                formset = order_form_set()
                # заполняем
                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_items[num].product
                    form.initial['quantity'] = basket_items[num].quantity
                # удаление собранных позиций из корзины. При удаление в данном
                # месте, возвращаясь в корзину после создания заказа, она будет
                # пуста
                basket_items.delete()
            else:
                formset = order_form_set()

        context_data['orderitems'] = formset  # если гет, то пустую форму
        context_data['title'] = 'заказ'
        return context_data

    def form_valid(self, form):  # в form главн. форма из get_context_data
        context = self.get_context_data()  # забраем контекст
        orderitems = context['orderitems']  # из него orderitems

        with transaction.atomic():
            # в форму добавляем пользователя из пост запроса
            form.instance.buyer = self.request.user
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

        # удаляем пустой заказ
        if self.object.get_total_cost() == 0:
            self.object.delete()

        return super(OrderItemsCreate, self).form_valid(form)


class OrderItemsUpdate(LoginRequiredMixin, UpdateView):
    model = Order
    # в соответствии с моделью все поля, кроме пользователя buyer, создаются
    # автоматически, buyer добавим позже
    fields = []
    success_url = reverse_lazy('orderapp:orders_list')

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)

    # добавляем данные в контекст, пересобираем в одну форму OrderItemForm
    # из Order и OrderItem
    def get_context_data(self, **kwargs):
        context_data = super(OrderItemsUpdate, self).get_context_data(**kwargs)
        order_form_set = inlineformset_factory(Order, OrderItem,
                                               form=OrderItemForm, extra=1)
        if self.request.POST:  # если пост запрос, заполняем данными
            formset = order_form_set(self.request.POST, instance=self.object)
        else:
            formset = order_form_set(instance=self.object)

        context_data['orderitems'] = formset  # если гет, то пустую форму
        context_data['title'] = 'редактировать заказ'
        return context_data

    def form_valid(self, form):  # в form главн. форма из get_context_data
        context = self.get_context_data()  # забраем контекст
        orderitems = context['orderitems']  # из него orderitems

        # with transaction.atomic():
        self.object = form.save()
        if orderitems.is_valid():
            orderitems.instance = self.object
            orderitems.save()

        # удаляем пустой заказ
        if self.object.get_total_cost() == 0:
            self.object.delete()

        return super(OrderItemsUpdate, self).form_valid(form)


# Шаблон удаления должен иметь имя вида «<имя класса>_confirm_delete.html»
class OrderItemsDelete(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('order:orders_list')

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)


# Шаблон по умолчанию для класса «DetailView»
# должен иметь имя вида  «<имя класса>_detail.html»
class OrderRead(LoginRequiredMixin, DetailView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)

# обновление статуса заказа при совершении покупки

def order_forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SEND_TO_PROCEED
    order.save()

    return HttpResponseRedirect(reverse('order:orders_list'))