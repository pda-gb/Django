from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory, ProductType


# Create your views here.
def main(request):
    title = 'Магазин Подушек'

    obj_products = Product.objects.all()[5:8]  # выведем на главной 3  товара

    variable_date = {
        'title': title,
        'obj_products': obj_products,
    }
    return render(request, 'mainapp/index.html', variable_date)

# сделать фильтрацию по типам последовательно после категорий
# добавить третье меню для выбора типа и направления сортировки (название, цена, скидки)
def products(request, pr_key=None):
    title = 'Товары'
    links_menu_type = ProductType.objects.all()
    links_menu_category = ProductCategory.objects.all()

    if pr_key is not None:
        if pr_key == 0:
            products_set = Product.objects.all()
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
            "category_of_products_set": category_of_products_set
        }
        return render(request, 'mainapp/product_list.html', variable_date)

    variable_date = {
        'title': title,
        'links_menu_category': links_menu_category,
        'links_menu_type': links_menu_type,
    }
    return render(request, 'mainapp/product_list.html', variable_date)


def contact(request):
    title = 'Контакты'
    variable_date = {
        'title': title,
    }
    return render(request, 'mainapp/contact.html', variable_date)
