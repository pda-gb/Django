from django.shortcuts import render
import mainapp.models

# Create your views here.
def main(request):
    title = 'Магазин Подушек'

    obj_products = mainapp.models.Product.objects.all()[:3]  #выведем на главной 3  товара

    variable_date = {
        'title': title,
        'obj_products': obj_products,
    }
    return render(request, 'mainapp/index.html', variable_date)


def products(request):
    title = 'Товары'
    links_menu_type = [
        {'href': '#', 'name': 'rewq'},
        {'href': '#', 'name': 'rwq'},
        {'href': '#', 'name': 'rewq'},

    ]
    links_menu_category = [
        {'href': '#', 'name': '3'},
        {'href': '#', 'name': '4'},
        {'href': '#', 'name': '5'},
        {'href': '#', 'name': '33'},
        {'href': '#', 'name': '44'},
    ]
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
