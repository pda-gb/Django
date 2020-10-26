from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.products, name='index'),
   path('page/<page>/', mainapp.products, name='index_page'),

   path('<int:pk_cat>/', mainapp.products, name='pr_category'),
   path('<int:pk_cat>/page/<page>/', mainapp.products, name='pr_category_page'),

   # path('<int:pk_type>/', mainapp.products, name='pr_type'),

   path('single_product/<int:pk_prod>/', mainapp.single_product, name='single_product'),
]
