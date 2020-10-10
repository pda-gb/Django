from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    title = "корзина"
    image_product = Product.objects
    variable_date = {
        "title": title

    }
    return render(request, 'basketapp/basket.html', variable_date)


def basket_add(request, pk_add):
    product_itm = get_object_or_404(Product, pk=pk_add)
    # проверка на наличие этого товара в магазине
    basket_itm = Basket.objects.filter(user=request.user, product=product_itm).first()
    # если нет, то создаём в корзине
    if not basket_itm:
        basket_itm = Basket.objects.create(user=request.user, product=product_itm)
    # увелич. кол.-во
    basket_itm.quantity += 1
    basket_itm.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk_del):
    variable_date = {}
    return render(request, 'basketapp/basket.html', variable_date)
