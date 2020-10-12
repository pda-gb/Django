import random
from django.shortcuts import render, get_object_or_404
from authapp.models import Buyer
from basketapp.models import Basket
from mainapp.models import Product, ProductCategory, ProductType


def get_trending_product():
    """
    Trending products in main page
    :return:
    """
    _products = Product.objects.all()
    trend = random.sample(list(_products), 6)  # [0]
    return trend


def get_products_in_main_page():
    """
    3 products in main page of main category only
    :return: 
    """
    main_prod = random.sample(list(Product.objects.filter(category_id=1)), 3)
    return main_prod


# def get_same_products()
#     """
#     same products in single product page
#     :return:
#     """
#     random
#     same = Product.objects.filter(category_id='#').exclude(pk='#')[:4]
#     return same

def get_basket(shop_user):
    _basket_itm = None
    if not shop_user.is_anonymous:
        _basket_itm = Basket.objects.filter(buyer=shop_user)  # собираем товары из корзины, для отображ. кол.-ва
    return _basket_itm


def main(request):
    title = 'Магазин Подушек'
    basket_itm = get_basket(request.user)  # узнаём кто зашёл, если зареган, выводим количество товаров у "корзинки"
    main_products = get_products_in_main_page()  # выведем на главной 3  товара
    trending_products = get_trending_product()  # выведем на главной 6 тренд. товара
    variable_date = {
        'title': title,
        'main_products': main_products,
        'basket_itm': basket_itm,
        'trending_products': trending_products
    }
    return render(request, 'mainapp/index.html', variable_date)


# сделать фильтрацию по типам последовательно после категорий
# добавить третье меню для выбора типа и направления сортировки (название, цена, скидки)
def products(request, pk_cat=None):
    title = 'Товары'
    links_menu_type = ProductType.objects.all()
    links_menu_category = ProductCategory.objects.all()
    products_set = Product.objects.all()
    basket_itm = get_basket(request.user)

    if pk_cat is not None:
        if pk_cat == 0:
            category_of_products_set = {
                "name": "все!"}  # при выборе дрю категории или заходе на продукты, эта строка не загружается
            # type_of_products_set = {"name": "все"}
        else:
            category_of_products_set = get_object_or_404(ProductCategory, pk=pk_cat)
            # type_of_products_set = get_object_or_404(ProductType, pk= #_key)
            products_set = Product.objects.all().filter(category=category_of_products_set)
        variable_date = {
            'title': title,
            'links_menu_category': links_menu_category,
            'links_menu_type': links_menu_type,
            "products_set": products_set,
            'category_of_products_set': category_of_products_set,
            'basket_itm': basket_itm
        }
        return render(request, 'mainapp/product_list.html', variable_date)

    variable_date = {
        'title': title,
        'links_menu_category': links_menu_category,
        'links_menu_type': links_menu_type,
        'products_set': products_set,  # что бы при первом открывании продуктов, были показаны   все продукты
        'basket_itm': basket_itm
    }
    return render(request, 'mainapp/product_list.html', variable_date)


def contact(request):
    title = 'Контакты'
    basket_itm = get_basket(request.user)
    variable_date = {
        'title': title,
        'basket_itm': basket_itm
    }
    return render(request, 'mainapp/contact.html', variable_date)


def single_product(request, pk_prod):
    single_prod = get_object_or_404(Product, pk=pk_prod)
    title = single_prod.name
    basket_itm = get_basket(request.user)
    variable_date = {
        'title': title,
        'basket_itm': basket_itm,
        'single_prod': single_prod
    }
    print('+++++#+++++++')
    print(single_prod.id)
    return render(request, 'mainapp/single_product.html', variable_date)

