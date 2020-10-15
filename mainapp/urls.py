from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.products, name='index'),
   path('<int:pk_cat>/', mainapp.products, name='pr_category'),
   path('single_product/<int:pk_prod>/', mainapp.single_product, name='single_product'),
]
