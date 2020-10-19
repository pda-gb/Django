from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.urls import reverse

from adminapp.forms import AdminEditFormProductCategory, AdminEditFormProductType, AdminEditFormProduct
from authapp.forms import BuyerRegistyForm, BuyerEditForm
from authapp.models import Buyer
from mainapp.models import ProductCategory, ProductType, Product


@user_passes_test(lambda x: x.is_superuser)
def admin(request):
    title = 'adm/ Админка'
    content = {
        'title': title,
    }
    return render(request, 'adminapp/admin.html', content)


# users =============== users =============== users =============== users =============== users
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
        'object': user_form
    }
    return render(request, 'adminapp/user.html', content)


@user_passes_test(lambda x: x.is_superuser)
def user_update(request, pk):
    title = 'adm/Редактирование пользователя'
    user = get_object_or_404(Buyer, pk=pk)
    if request.method == 'POST':
        user_form = BuyerRegistyForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[user.pk]))
    else:
        user_form = BuyerRegistyForm(instance=user)
    content = {
        'title': title,
        'objects': user_form
    }
    return render(request, 'adminapp/user.html', content)

@user_passes_test(lambda x: x.is_superuser)
def user_delete(request, pk):
    title = 'adm/Удаление пользователя'
    user = get_object_or_404(Buyer, pk=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users_read'))
    content = {
        'title': title,
        'object_del': user
    }
    return render(request, 'adminapp/user_delete.html', content)


# products =============== products =============== products =============== products
@user_passes_test(lambda x: x.is_superuser)
def products_read(request, pk):
    title = 'adm/товары'
    products = Product.objects.filter(category=pk)
    content = {
        'title': title,
        'objects': products,
    }
    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda x: x.is_superuser)
def product_read(request, pk):
    title = 'adm/товар'
    product = Product.objects.filter(pk=pk).first()
    content = {
        'title': title,
        'objects': product
    }
    return render(request, 'adminapp/product.html', content)


@user_passes_test(lambda x: x.is_superuser)
def product_create(request, pk):
    title = 'adm/Новый товар'
    if request.method == 'POST':
        product_form = AdminEditFormProduct(request.POST, request.FILES, instance=pk)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:categories_read'))
    else:
        product_form = AdminEditFormProduct()
    content = {
        'title': title,
        'objects': product_form
    }
    return render(request, 'adminapp/product.html', content)


@user_passes_test(lambda x: x.is_superuser)
def product_update(request, pk):
    title = 'adm/Редактирование товара'
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product_form = AdminEditFormProduct(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:products_read'))
    else:
        product_form = AdminEditFormProductCategory(instance=product)
    content = {
        'title': title,
        'objects': product_form
    }
    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda x: x.is_superuser)
def product_delete(request, pk):
    title = 'adm/Удаление товара'
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('admin:product_read'))
    content = {
        'title': title,
        'object_del': product
    }
    return render(request, 'adminapp/product_delete.html', content)


# categories =============== categories =============== categories =============== categories
@user_passes_test(lambda x: x.is_superuser)
def categories_read(request):
    title = 'adm/Категории товаров'
    categories_list = ProductCategory.objects.all()
    content = {
        'title': title,
        'objects': categories_list
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
    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('admin:categories_read'))
    content = {
        'title': title,
        'object_del': category
    }
    return render(request, 'adminapp/category_delete.html', content)


# type =============== type =============== type =============== type =============== type
@user_passes_test(lambda x: x.is_superuser)
def types_read(request):
    title = 'adm/Тип материалов товаров'
    types_list = ProductType.objects.all()
    content = {
        'title': title,
        'objects': types_list
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
    type = get_object_or_404(ProductType, pk=pk)
    if request.method == 'POST':
        type_form = AdminEditFormProductType(request.POST, request.FILES, instance=type)
        if type_form.is_valid():
            type_form.save()
            return HttpResponseRedirect(reverse('admin:types_read'))
    else:
        type_form = AdminEditFormProductType(instance=type)
    content = {
        'title': title,
        'objects': type_form
    }
    return render(request, 'adminapp/category.html', content)


@user_passes_test(lambda x: x.is_superuser)
def type_delete(request, pk):
    title = 'adm/Удаление типа'
    type = get_object_or_404(ProductType, pk=pk)
    if request.method == 'POST':
        type.is_active = False
        type.save()
        return HttpResponseRedirect(reverse('admin:types_read'))
    content = {
        'title': title,
        'object_del': type
    }
    return render(request, 'adminapp/type_delete.html', content)
