from basketapp.models import Basket


def get_basket_itm(request):
    '''
    Во все контроллеры mainapp добавляется контекст
    '''
    # создаём пустой оъект корзины
    basket_itm = []

    if not request.user.is_anonymous:
        basket_itm = Basket.objects.filter(buyer=request.user)  # собираем товары из корзины, для отображ. кол.-ва
    return {
        'basket_itm': basket_itm
    }