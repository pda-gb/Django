from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from adminapp.forms import AdminEditFormProductCategory, AdminEditFormProductType, AdminEditFormProduct, \
    AdminEditFormBuyer
from authapp.forms import BuyerRegistyForm
from authapp.models import Buyer
from mainapp.models import ProductCategory, ProductType, Product


@user_passes_test(lambda x: x.is_superuser)
def admin(request):
    title = 'adm/ Админка'
    content = {
        'title': title,
    }
    return render(request, 'adminapp/admin.html', content)


def get_paginator_page(_objs, _page):
    _paginator = Paginator(_objs, 2)
    try:  # вывести страницу продуктов номер page
        _objs_paginator = _paginator.page(_page)
    except PageNotAnInteger:  # если страница не целое число, то вывести первую
        _objs_paginator = _paginator.page(1)
    except EmptyPage:  # если больше максимальной, то последнюю
        _objs_paginator = _paginator.page(_paginator.num_pages)
    return _objs_paginator


# users =============== users =============== users =============== users =============== users
@user_passes_test(lambda x: x.is_superuser)
def users_read(request, page=1):
    title = 'adm/пользователи'
    users_list = Buyer.objects.all().order_by('-is_active', '-is_superuser', 'username', 'first_name', 'last_name')
    users_list_paginator = get_paginator_page(users_list, page)
    content = {
        'title': title,
        'objects': users_list_paginator
    }
    return render(request, 'adminapp/users.html', content)


@user_passes_test(lambda x: x.is_superuser)
def user_create(request):
    title = 'adm/Новый пользователь'
    if request.method == 'POST':
        user_form = BuyerRegistyForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users_read'))
    else:
        user_form = BuyerRegistyForm()
    content = {
        'title': title,
        'objects': user_form
    }
    return render(request, 'adminapp/user.html', content)


@user_passes_test(lambda x: x.is_superuser)
def user_update(request, pk):
    title = 'adm/Редактирование пользователя'
    user = get_object_or_404(Buyer, pk=pk)

    if request.method == 'POST':
        user_form = AdminEditFormBuyer(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[user.pk]))
    else:
        user_form = AdminEditFormBuyer(instance=user)
    content = {
        'title': title,
        'objects': user_form,
    }
    return render(request, 'adminapp/user.html', content)


@user_passes_test(lambda x: x.is_superuser)
def user_delete(request, pk):
    title = 'adm/Удаление пользователя'
    user = get_object_or_404(Buyer, pk=pk)
    if user.is_active is True:
        if request.method == 'POST':
            user.is_active = False
            user.save()
            return HttpResponseRedirect(reverse('admin:users_read'))
        content = {
            'title': title,
            'object_del': user
        }
        return render(request, 'adminapp/user_delete.html', content)
    else:
        # if request.method == 'POST':
        user.is_active = True
        user.save()
        return HttpResponseRedirect(reverse('admin:users_read'))


# products =============== products =============== products =============== products
@user_passes_test(lambda x: x.is_superuser)
def products_category_read(request, pk, page=1):
    title = 'adm/товары категории'
    products = Product.objects.filter(category=pk).order_by('-is_active', 'name')
    products_page = get_paginator_page(products, page)
    # if products.exists():
    #     pk_category = products[0].category_id
    pk_category = pk
    content = {
        'title': title,
        'objects_of_category': products_page,  # загружать на странице сипсок  по категориям
        'objects_of_type': None,  # не загружать на странице сипсок  по типам
        'pk_category': pk_category  # для передачи pk категории в шаблон, что бы  потомвернуться к списку товаров
    }
    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda x: x.is_superuser)
def products_type_read(request, pk, page=1):
    title = 'adm/товары типа'
    products = Product.objects.filter(type=pk).order_by('-is_active', 'name')
    products_page = get_paginator_page(products, page)
    # if products.exists():
    #     pk_type = products[0].type_id
    pk_type = pk
    content = {
        'title': title,
        'objects_of_type': products_page,
        'objects_of_category': None,
        'pk_type': pk_type
    }
    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda x: x.is_superuser)
def product_create(request, pk):
    title = 'adm/Новый товар'
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        product_form = AdminEditFormProduct(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:products_category_read', args=[pk]))
    else:
        product_form = AdminEditFormProduct(initial={'category': category})
    content = {
        'title': title,
        'objects': product_form,
        'pk_category': category.pk
    }
    return render(request, 'adminapp/product.html', content)


@user_passes_test(lambda x: x.is_superuser)
def product_update(request, pk):
    title = 'adm/Редактирование товара'
    product = get_object_or_404(Product, pk=pk)
    pk_category = product.category_id
    if request.method == 'POST':
        product_form = AdminEditFormProduct(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:product_update', args=[product.pk]))
    else:
        product_form = AdminEditFormProduct(instance=product)
    content = {
        'title': title,
        'objects': product_form,
        'pk_category': pk_category,
    }
    return render(request, 'adminapp/product.html', content)


@user_passes_test(lambda x: x.is_superuser)
def product_tp_delete(request, pk, pk_type):
    title = 'adm/Удаление товара'
    product = get_object_or_404(Product, pk=pk)
    if product.is_active is True:
        if request.method == 'POST':
            product.is_active = False
            product.save()
            return HttpResponseRedirect(reverse('admin:products_type_read', args=[pk_type]))
        content = {
            'title': title,
            'object_del': product,
            'pk_type': pk_type
        }
        return render(request, 'adminapp/product_delete.html', content)
    else:
        # if request.method == 'POST':
        product.is_active = True
        product.save()
        return HttpResponseRedirect(reverse('admin:products_type_read', args=[pk_type]))


@user_passes_test(lambda x: x.is_superuser)
def product_ct_delete(request, pk, pk_category):
    title = 'adm/Удаление товара'
    product = get_object_or_404(Product, pk=pk)
    if product.is_active is True:
        if request.method == 'POST':
            product.is_active = False
            product.save()
            return HttpResponseRedirect(reverse('admin:products_category_read', args=[pk_category]))
        content = {
            'title': title,
            'object_del': product,
            'pk_category': pk_category
        }
        return render(request, 'adminapp/product_delete.html', content)
    else:
        # if request.method == 'POST':
        product.is_active = True
        product.save()
        return HttpResponseRedirect(reverse('admin:products_category_read', args=[pk_category]))


# categories =============== categories =============== categories =============== categories
@user_passes_test(lambda x: x.is_superuser)
def categories_read(request, page=1):
    title = 'adm/Категории товаров'
    categories_list = ProductCategory.objects.all().order_by('-is_active', 'name')
    categories_list_page = get_paginator_page(categories_list, page)
    content = {
        'title': title,
        'objects': categories_list_page
    }
    return render(request, 'adminapp/categories.html', content)


@user_passes_test(lambda x: x.is_superuser)
def category_create(request):
    title = 'adm/Новая категория'
    if request.method == 'POST':
        category_form = AdminEditFormProductCategory(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:categories_read'))
    else:
        category_form = AdminEditFormProductCategory()
    content = {
        'title': title,
        'objects': category_form
    }
    return render(request, 'adminapp/category.html', content)


@user_passes_test(lambda x: x.is_superuser)
def category_update(request, pk):
    title = 'adm/Редактирование категории'
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        category_form = AdminEditFormProductCategory(request.POST, request.FILES, instance=category)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:categories_read'))
    else:
        category_form = AdminEditFormProductCategory(instance=category)
    content = {
        'title': title,
        'objects': category_form
    }
    return render(request, 'adminapp/category.html', content)


@user_passes_test(lambda x: x.is_superuser)
def category_delete(request, pk):
    title = 'adm/Удаление категории'
    category = get_object_or_404(ProductCategory, pk=pk)
    if category.is_active is True:
        if request.method == 'POST':
            category.is_active = False
            category.save()
            return HttpResponseRedirect(reverse('admin:categories_read'))
        content = {
            'title': title,
            'object_del': category
        }
        return render(request, 'adminapp/category_delete.html', content)
    else:
        # if request.method == 'POST':
        category.is_active = True
        category.save()
        return HttpResponseRedirect(reverse('admin:categories_read'))


# type =============== type =============== type =============== type =============== type
@user_passes_test(lambda x: x.is_superuser)
def types_read(request, page=1):
    title = 'adm/Тип материалов товаров'
    types_list = ProductType.objects.all().order_by('-is_active', 'name')
    types_list_page = get_paginator_page(types_list, page)
    content = {
        'title': title,
        'objects': types_list_page
    }
    return render(request, 'adminapp/types.html', content)


@user_passes_test(lambda x: x.is_superuser)
def type_create(request):
    title = 'adm/Новый тип'
    if request.method == 'POST':
        type_form = AdminEditFormProductType(request.POST, request.FILES)
        if type_form.is_valid():
            type_form.save()
            return HttpResponseRedirect(reverse('admin:types_read'))
    else:
        type_form = AdminEditFormProductType()
    content = {
        'title': title,
        'objects': type_form
    }
    return render(request, 'adminapp/type.html', content)


@user_passes_test(lambda x: x.is_superuser)
def type_update(request, pk):
    title = 'adm/Редактирование типа'
    type_upd = get_object_or_404(ProductType, pk=pk)
    if request.method == 'POST':
        type_form = AdminEditFormProductType(request.POST, request.FILES, instance=type_upd)
        if type_form.is_valid():
            type_form.save()
            return HttpResponseRedirect(reverse('admin:types_read'))
    else:
        type_form = AdminEditFormProductType(instance=type_upd)
    content = {
        'title': title,
        'objects': type_form
    }
    return render(request, 'adminapp/type.html', content)


@user_passes_test(lambda x: x.is_superuser)
def type_delete(request, pk):
    title = 'adm/Удаление типа'
    type_del = get_object_or_404(ProductType, pk=pk)
    if type_del.is_active is True:
        if request.method == 'POST':
            type_del.is_active = False
            type_del.save()
            return HttpResponseRedirect(reverse('admin:types_read'))
        content = {
            'title': title,
            'object_del': type_del
        }
        return render(request, 'adminapp/type_delete.html', content)
    else:
        # if request.method == 'POST':
        type_del.is_active = True
        type_del.save()
        return HttpResponseRedirect(reverse('admin:types_read'))
