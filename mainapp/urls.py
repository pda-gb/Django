from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.products, name='index'),
   path('<int:pr_key>/', mainapp.products, name='pr_category'),
]
