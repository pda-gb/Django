from django.shortcuts import render, get_object_or_404

from authapp.models import Buyer
from basketapp.models import Basket
from mainapp.models import Product, ProductCategory, ProductType


# Create your views here.
def main(request):
    title = 'Магазин Подушек'
    shop_user = request.user  # узнаём кто зашёл, если зареган, выводим количество товаров у "корзинки"
    basket_itm = None
    if not shop_user.is_anonymous:
        basket_itm = Basket.objects.filter(buyer=shop_user)  # собираем товары из корзины, для отображ. кол.-ва
    obj_products = Product.objects.all()[5:8]  # выведем на главной 3  товара
    variable_date = {
        'title': title,
        'obj_products': obj_products,
        'basket_itm': basket_itm
    }
    return render(request, 'mainapp/index.html', variable_date)

# сделать фильтрацию по типам последовательно после категорий
# добавить третье меню для выбора типа и направления сортировки (название, цена, скидки)
def products(request, pr_key=None):
    title = 'Товары'
    links_menu_type = ProductType.objects.all()
    links_menu_category = ProductCategory.objects.all()
    products_set = Product.objects.all()

    shop_user = request.user  # узнаём кто зашёл, если зареган, выводим количество товаров у "корзинки"
    basket_itm = None
    if not shop_user.is_anonymous:
        basket_itm = Basket.objects.filter(buyer=request.user)  # собираем товары из корзины, для отображ. кол.-ва
    if pr_key is not None:
        if pr_key == 0:
            category_of_products_set = {"name": "все!"}  # при выборе дрю категории или заходе на продукты, эта строка не загружается
            # type_of_products_set = {"name": "все"}
        else:
            category_of_products_set = get_object_or_404(ProductCategory, pk=pr_key)
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
    shop_user = request.user  # узнаём кто зашёл, если зареган, выводим количество товаров у "корзинки"
    basket_itm = None
    if not shop_user.is_anonymous:
        basket_itm = Basket.objects.filter(buyer=request.user)  # собираем товары из корзины, для отображ. кол.-ва
    variable_date = {
        'title': title,
        'basket_itm': basket_itm
    }
    return render(request, 'mainapp/contact.html', variable_date)
