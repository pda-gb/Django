from django.shortcuts import render


# Create your views here.
def main(request):
    variable_date = {
        'title': 'Магазин Подушек',
    }
    return render(request, 'mainapp/index.html', variable_date)


def products(request):
     variable_date = {
         'title': 'Товары',
     }
     return render(request, 'mainapp/product_list.html', variable_date)


def contact(request):
     variable_date = {
        'title': 'Контакты',
     }
     return render(request, 'mainapp/contact.html', variable_date)
