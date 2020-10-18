from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/read/', adminapp.users_read, name='users_read'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),

    path('products/create/', adminapp.products_create, name='products_create'),
    path('products/read/category/<int:pk>/', adminapp.products_read, name='products_read'),
    path('products/read/<int:pk>/', adminapp.product_read, name='product_read'),
    path('products/update/<int:pk>/', adminapp.products_update, name='products_update'),
    path('products/delete/<int:pk>/', adminapp.products_delete, name='products_delete'),

    path('prod_cat/create/', adminapp.prod_cat_create, name='prod_cat_create'),
    path('prod_cat/read/', adminapp.prod_cat_read, name='prod_cats_read'),
    path('prod_cat/update/<int:pk>/', adminapp.prod_cat_update, name='prod_cat_update'),
    path('prod_cat/delete/<int:pk>/', adminapp.prod_cat_delete, name='prod_cat_delete'),

    path('prod_type/create/', adminapp.prod_type_create, name='prod_type_create'),
    path('prod_type/read/', adminapp.prod_type_read, name='prod_types_read'),
    path('prod_type/update/<int:pk>/', adminapp.prod_type_update, name='prod_type_update'),
    path('prod_type/delete/<int:pk>/', adminapp.prod_type_delete, name='prod_type_delete'),

]