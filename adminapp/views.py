from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404

# users ===============
from authapp.models import Buyer
from mainapp.models import ProductCategory, ProductType, Product


@user_passes_test(lambda x: x.is_superuser)
def users_read(request):
    title = 'adm/пользователи'
    users_list = Buyer.objects.all()
    content = {
        'title': title,
        'objects': users_list
    }
    return render(request, 'adminapp/users.html', content)


@user_passes_test(lambda x: x.is_superuser)
def user_create(request):
    pass


@user_passes_test(lambda x: x.is_superuser)
def user_update(request, pk):
    pass


@user_passes_test(lambda x: x.is_superuser)
def user_delete(request, pk):
    pass


# products ===============
@user_passes_test(lambda x: x.is_superuser)
def products_read(request, pk):
    title = 'adm/товары'
    categories_itm = get_object_or_404(ProductCategory, pk)
    product = Product.objects.filter(category=categories_itm)
    content = {
        'title': title,
        'objects': product,
        'category': categories_itm
    }
    return render(request, 'adminapp/product.html', content)


@user_passes_test(lambda x: x.is_superuser)
def product_read(request, pk):
    title = 'adm/товар'
    product = Product.objects.filter(pk=pk)
    content = {
        'title': title,
        'objects': product
    }
    return render(request, 'adminapp/product.html', content)


@user_passes_test(lambda x: x.is_superuser)
def products_create(request, pk):
    pass


@user_passes_test(lambda x: x.is_superuser)
def products_update(request, pk):
    pass


@user_passes_test(lambda x: x.is_superuser)
def products_delete(request, pk):
    pass


# prod_cat ===============
@user_passes_test(lambda x: x.is_superuser)
def prod_cat_read(request):
    title = 'adm/Категории товаров'
    categories_list = ProductCategory.objects.all()
    content = {
        'title': title,
        'objects': categories_list
    }
    return render(request, 'adminapp/categories.html', content)


@user_passes_test(lambda x: x.is_superuser)
def prod_cat_create(request):
    pass


@user_passes_test(lambda x: x.is_superuser)
def prod_cat_update(request, pk):
    pass


@user_passes_test(lambda x: x.is_superuser)
def prod_cat_delete(request, pk):
    pass


# prod_type ===============
@user_passes_test(lambda x: x.is_superuser)
def prod_type_read(request):
    title = 'adm/Тип материалов товаров'
    types_list = ProductType.objects.all()
    content = {
        'title': title,
        'objects': types_list
    }
    return render(request, 'adminapp/types.html', content)


@user_passes_test(lambda x: x.is_superuser)
def prod_type_create(request):
    pass


@user_passes_test(lambda x: x.is_superuser)
def prod_type_update(request, pk):
    pass


@user_passes_test(lambda x: x.is_superuser)
def prod_type_delete(request, pk):
    pass
