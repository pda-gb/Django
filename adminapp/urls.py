from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.admin, name='admin'),

    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/read/', adminapp.users_read, name='users_read'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),

    path('products/create/<int:pk>/', adminapp.product_create, name='product_create'),
    path('products/read/category/<int:pk>/', adminapp.products_category_read, name='products_category_read'),
    path('products/read/type/<int:pk>/', adminapp.products_type_read, name='products_type_read'),
    path('products/update/<int:pk>/', adminapp.product_update, name='product_update'),
    path('products/delete/ct/<int:pk_category>/<int:pk>/', adminapp.product_ct_delete, name='product_ct_delete'),
    path('products/delete/tp/<int:pk_type>/<int:pk>/', adminapp.product_tp_delete, name='product_tp_delete'),
    # path('products/return/tp/<int:pk_type>/<int:pk>/', adminapp.product_tp_return, name='product_tp_return'),

    path('categories/create/', adminapp.category_create, name='category_create'),
    path('categories/read/', adminapp.categories_read, name='categories_read'),
    path('categories/update/<int:pk>/', adminapp.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', adminapp.category_delete, name='category_delete'),

    path('types/create/', adminapp.type_create, name='type_create'),
    path('types/read/', adminapp.types_read, name='types_read'),
    path('types/update/<int:pk>/', adminapp.type_update, name='type_update'),
    path('types/delete/<int:pk>/', adminapp.type_delete, name='type_delete'),

]
