import random

from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory, ProductType


def get_trending_product():
    """
    Trending products in main page
    :return:
    """
    _products = Product.objects.filter(is_active=True)
    trend = random.sample(list(_products), 6)  # [0]
    return trend


def get_products_in_main_page():
    """
    3 products in main page of main category only
    :return: 
    """
    main_prod = random.sample(list(Product.objects.filter(category_id=1, is_active=True)), 3)
    return main_prod


# def get_same_products()
#     """
#     same products in single product page
#     :return:
#     """
#     random
#     same = Product.objects.filter(category_id='#').exclude(pk='#')[:4]
#     return same

def get_basket_itm(shop_user):
    # создаём пустой оъект корзины
    _basket_itm = None
    if not shop_user.is_anonymous:
        _basket_itm = Basket.objects.filter(buyer=shop_user)  # собираем товары из корзины, для отображ. кол.-ва
    return _basket_itm


def main(request):
    title = 'Магазин Подушек'
    basket_itm = get_basket_itm(request.user)  # узнаём кто зашёл, если зареган, выводим количество товаров у "корзинки"
    main_products = get_products_in_main_page()  # выведем на главной 3  товара
    trending_products = get_trending_product()  # выведем на главной 6 тренд. товара
    variable_date = {
        'title': title,
        'main_products': main_products,
        'basket_itm': basket_itm,
        'trending_products': trending_products
    }
    return render(request, 'mainapp/index.html', variable_date)


def get_paginator_page(_products, _page):
    _paginator = Paginator(_products, 4)
    try:  # вывести страницу продуктов номер page
        _products_paginator = _paginator.page(_page)
    except PageNotAnInteger:  # если страница не целое число, то вывести первую
        _products_paginator = _paginator.page(1)
    except EmptyPage:  # если больше максимальной, то последнюю
        _products_paginator = _paginator.page(_paginator.num_pages)
    return _products_paginator


# сделать фильтрацию по типам последовательно после категорий
# добавить третье меню для выбора типа и направления сортировки (название, цена, скидки)
def products(request, pk_cat=None, page=1):
    title = 'Товары'
    links_menu_type = ProductType.objects.filter(is_active=True)
    links_menu_category = ProductCategory.objects.filter(is_active=True)
    basket_itm = get_basket_itm(request.user)

    if pk_cat is None:
        products_set = Product.objects.filter(is_active=True, category__is_active=True)
        products_paginator = get_paginator_page(products_set, page)

    if pk_cat is not None:
        if pk_cat == 0:
            # при выборе дрю категории или заходе на продукты, эта строка не загружается
            category_of_products_set = {"name": "все!"}
            products_set = Product.objects.filter(is_active=True, category__is_active=True)
            products_paginator = get_paginator_page(products_set, page)
            # type_of_products_set = {"name": "все"}
        else:
            category_of_products_set = get_object_or_404(ProductCategory, pk=pk_cat)
            # type_of_products_set = get_object_or_404(ProductType, pk= #_key)
            products_set = Product.objects.filter(category=category_of_products_set, is_active=True,
                                                  category__is_active=True)
            products_paginator = get_paginator_page(products_set, page)

        variable_date = {
            'title': title,
            'pk_cat': pk_cat,
            'links_menu_category': links_menu_category,
            'links_menu_type': links_menu_type,
            "products_set": products_paginator,
            'category_of_products_set': category_of_products_set,
            'basket_itm': basket_itm
        }
        return render(request, 'mainapp/product_list.html', variable_date)

    variable_date = {
        'title': title,
        'pk_cat': pk_cat,
        'links_menu_category': links_menu_category,
        'links_menu_type': links_menu_type,
        'products_set': products_paginator,  # что бы при первом открывании продуктов, были показаны   все продукты
        'basket_itm': basket_itm
    }
    return render(request, 'mainapp/product_list.html', variable_date)


def contact(request):
    title = 'Контакты'
    basket_itm = get_basket_itm(request.user)
    variable_date = {
        'title': title,
        'basket_itm': basket_itm
    }
    return render(request, 'mainapp/contact.html', variable_date)


class SingleProductDetailView(DetailView):
    model = Product
    template_name = 'mainapp/single_product.html'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Товар'
        return context_data


# def single_product(request, pk_prod):
#     single_prod = get_object_or_404(Product, pk=pk_prod)
#     title = single_prod.name
#     basket_itm = get_basket_itm(request.user)
#     variable_date = {
#         'title': title,
#         'basket_itm': basket_itm,
#         'single_prod': single_prod
#     }
#     return render(request, 'mainapp/single_product.html', variable_date)
