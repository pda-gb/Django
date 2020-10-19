from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/read/', adminapp.users_read, name='users_read'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),

    path('products/create/category/<int:pk>/', adminapp.products_create, name='products_create'),
    path('products/read/category/<int:pk>/', adminapp.products_read, name='products_read'),
    path('products/read/<int:pk>/', adminapp.product_read, name='product_read'),
    path('products/update/<int:pk>/', adminapp.products_update, name='products_update'),
    path('products/delete/<int:pk>/', adminapp.products_delete, name='products_delete'),

    path('categories/create/', adminapp.prod_cat_read, name='prod_cat_create'),
    path('categories/read/', adminapp.prod_cat_read, name='prod_cats_read'),
    path('categories/update/<int:pk>/', adminapp.prod_cat_update, name='prod_cat_update'),
    path('categories/delete/<int:pk>/', adminapp.prod_cat_delete, name='prod_cat_delete'),

    path('types/create/', adminapp.prod_type_create, name='prod_type_create'),
    path('types/read/', adminapp.prod_type_read, name='prod_types_read'),
    path('types/update/<int:pk>/', adminapp.prod_type_update, name='prod_type_update'),
    path('types/delete/<int:pk>/', adminapp.prod_type_delete, name='prod_type_delete'),

]