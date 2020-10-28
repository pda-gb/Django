from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.admin, name='admin'),

    path('users/create/', adminapp.UserCreateView.as_view(), name='user_create'),
    # path('users/read/', adminapp.users_read, name='users_read'),
    path('users/read/', adminapp.UsersListView.as_view(), name='users_read'),
    # path('users/read/page/<page>/', adminapp.users_read, name='users_read_page'),
    path('users/read/page/<page>/', adminapp.UsersListView.as_view(), name='users_read_page'),
    # path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/update/<int:pk>/', adminapp.UserUpdateView.as_view(), name='user_update'),
    # path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),
    path('users/delete/<int:pk>/', adminapp.UserDeleteView.as_view(), name='user_delete'),
    path('users/return/<int:pk>/', adminapp.UserReturnView.as_view(), name='user_return'),

    path('products/create/<int:pk>/', adminapp.product_create, name='product_create'),
    path('products/read/category/<int:pk>/', adminapp.products_category_read, name='products_category_read'),
    path('products/read/category/<int:pk>/page/<page>/', adminapp.products_category_read, name='products_category_read_page'),
    path('products/read/type/<int:pk>/', adminapp.products_type_read, name='products_type_read'),
    path('products/read/type/<int:pk>/page/<page>/', adminapp.products_type_read, name='products_type_read_read_page'),
    path('products/update/<int:pk>/', adminapp.product_update, name='product_update'),
    path('products/delete/ct/<int:pk_category>/<int:pk>/', adminapp.product_ct_delete, name='product_ct_delete'),
    path('products/delete/tp/<int:pk_type>/<int:pk>/', adminapp.product_tp_delete, name='product_tp_delete'),

    path('categories/create/', adminapp.CategoryCreateView.as_view(), name='category_create'),
    # path('categories/create/', adminapp.category_create, name='category_create'),
    path('categories/read/', adminapp.categories_read, name='categories_read'),
    path('categories/read/page/<page>/', adminapp.categories_read, name='categories_read_page'),
    # path('categories/update/<int:pk>/', adminapp.category_update, name='category_update'),
    path('categories/update/<int:pk>/', adminapp.CategoryUpdateView.as_view(), name='category_update'),
    # path('categories/delete/<int:pk>/', adminapp.category_delete, name='category_delete'),
    path('categories/delete/<int:pk>/', adminapp.CategoryDeleteView.as_view(), name='category_delete'),

    path('types/create/', adminapp.type_create, name='type_create'),
    path('types/read/', adminapp.types_read, name='types_read'),
    path('types/read/page/<page>/', adminapp.types_read, name='types_read_page'),
    path('types/update/<int:pk>/', adminapp.type_update, name='type_update'),
    path('types/delete/<int:pk>/', adminapp.type_delete, name='type_delete'),

]
