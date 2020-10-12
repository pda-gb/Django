from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product


def check_authorisations(_user):
     # узнаём кто зашёл, если зареган, выводим количество товаров у "корзинки"
    _basket_itm = None
    if not _user.is_anonymous:
        _basket_itm = Basket.objects.filter(buyer=_user)  # собираем товары из корзины, для отображ. кол.-ва
    return _basket_itm

def basket(request):
    title = 'корзина'
    basket_itm = check_authorisations(request.user)
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
    basket_itm = check_authorisations(request.user)
    # увелич. кол.-во
    basket_itm.quantity += 1
    basket_itm.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk_del):
    variable_date = {}
    return render(request, 'basketapp/basket.html', variable_date)

    # print('+++++#+++++++')
    # print()
