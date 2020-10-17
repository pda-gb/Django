from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.template.loader import render_to_string
from basketapp.models import Basket
from mainapp.models import Product


def get_authorised_prod(_user):
    # узнаём кто зашёл, если зареган, выводим количество "товаров-корзинок"
    _basket_itm = None
    if not _user.is_anonymous:
        _basket_itm = Basket.objects.filter(buyer=_user)  # собираем товары из корзины, для отображ. кол.-ва
    return _basket_itm


@login_required
def basket(request):
    title = 'корзина'
    basket_itm = get_authorised_prod(request.user)
    variable_date = {
        'title': title,
        'basket_itm': basket_itm
    }
    return render(request, 'basketapp/basket.html', variable_date)


@login_required
def basket_add(request, pk_add):
    # проверка на наличие этого товара в магазине
    product_itm = get_object_or_404(Product, pk=pk_add)
    # проверяем, есть ли такой уже в корзине.
    basket_itm = Basket.objects.filter(buyer=request.user, product=product_itm).first()
    #  если нет, то создаём в корзине товар-корзинку
    if not basket_itm:
        basket_itm = Basket.objects.create(buyer=request.user, product=product_itm)
    # увелич. кол.-во

    basket_itm.quantity += 1
    basket_itm.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk_del):
    rm_product = get_object_or_404(Basket, pk=pk_del)
    rm_product.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    # защита от введения прямой ссылки пользователем
    if request.is_ajax():
        # для для защиты от возможного преобраз. в сторку в JS
        quantity = int(quantity)
        new_basket_itm = Basket.objects.get(pk=int(pk))
        if quantity > 0:
            new_basket_itm.quantity = quantity
            new_basket_itm.save()
        else:
            # удалить товар, если кол.-во <= 0.
            new_basket_itm.delete()
        basket_itm = Basket.objects.filter(buyer=request.user)
        variable_date = {
            'basket_itm': basket_itm
        }
        result = render_to_string('basketapp/includes/inc_basket.html', variable_date)
        return JsonResponse({'result': result})

    # print('+++++#+++++++')
    # print()
