from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


# users ===============
from authapp.models import Buyer


@user_passes_test(lambda x: x.is_superuser)
def users_read(request):
    title = 'adm/пользователи'
    users_list = Buyer.objects.all()
    content = {
        'title': title,
        'objects': users_list
    }
    return render(request, 'adminapp/admin.html', content)


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
    pass


@user_passes_test(lambda x: x.is_superuser)
def product_read(request, pk):
    pass


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
    pass


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
    pass


@user_passes_test(lambda x: x.is_superuser)
def prod_type_create(request):
    pass


@user_passes_test(lambda x: x.is_superuser)
def prod_type_update(request, pk):
    pass


@user_passes_test(lambda x: x.is_superuser)
def prod_type_delete(request, pk):
    pass
