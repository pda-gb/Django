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
    path('products/read/category/<int:pk>/', adminapp.products_read, name='products_read'),
    path('products/read/<int:pk>/', adminapp.product_read, name='product_read'),
    path('products/update/<int:pk>/', adminapp.product_update, name='product_update'),
    path('products/delete/<int:pk>/', adminapp.product_delete, name='product_delete'),

    path('categories/create/', adminapp.category_create, name='category_create'),
    path('categories/read/', adminapp.categories_read, name='categories_read'),
    path('categories/update/<int:pk>/', adminapp.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', adminapp.category_delete, name='category_delete'),

    path('types/create/', adminapp.type_create, name='type_create'),
    path('types/read/', adminapp.types_read, name='types_read'),
    path('types/update/<int:pk>/', adminapp.type_update, name='type_update'),
    path('types/delete/<int:pk>/', adminapp.type_delete, name='type_delete'),

]