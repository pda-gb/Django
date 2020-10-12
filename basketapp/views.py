from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product


def get_authorised_prod(_user):
     # узнаём кто зашёл, если зареган, выводим количество товаров у "корзинки"
    _basket_itm = None
    if not _user.is_anonymous:
        _basket_itm = Basket.objects.filter(buyer=_user).order_by('product__category')  # собираем товары из корзины, для отображ. кол.-ва
    return _basket_itm

def basket(request):
    title = 'корзина'
    basket_itm = get_authorised_prod(request.user)
    variable_date = {
        'title': title,
        'basket_itm': basket_itm
    }
    return render(request, 'basketapp/basket.html', variable_date)


def basket_add(request, pk_add):
    # проверка на наличие этого товара в магазине
    product_itm = get_object_or_404(Product, pk=pk_add)
    basket_itm = Basket.objects.filter(buyer=request.user, product=product_itm).first()
    # если нет, то создаём в корзине
    basket_itm = get_authorised_prod(request.user)
    # увелич. кол.-во
    basket_itm.quantity += 1
    basket_itm.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk_del):
    rm_product = get_object_or_404(Basket, pk=pk_del)
    rm_product.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # print('+++++#+++++++')
    # print()
