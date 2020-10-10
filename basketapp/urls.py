from django.urls import path
import basketapp.views as basket_v

app_name = 'basket'

urlpatterns = [
    path('', basket_v.basket, name='main'),
    path('add/<int:pk_basket>/', basket_v.basket_add, name='add'),
    path('remove/<int:pk_basket>)/', basket_v.basket_remove, name='remove'),

]
