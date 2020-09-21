from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/product_list.html')


def contact(request):
    return render(request, 'mainapp/contact.html')
