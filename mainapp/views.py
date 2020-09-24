from django.shortcuts import render


# Create your views here.
def main(request):
    variable_date = {
        'title': 'Магазин Подушек',
    }
    return render(request, 'mainapp/index.html', variable_date)


def products(request):
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
        'title': 'Товары',
        'links_menu_category': links_menu_category,
        'links_menu_type': links_menu_type,
    }
    return render(request, 'mainapp/product_list.html', variable_date)


def contact(request):
    variable_date = {
        'title': 'Контакты',
    }
    return render(request, 'mainapp/contact.html', variable_date)
