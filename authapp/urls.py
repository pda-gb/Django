from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('registry/', authapp.registry, name='registry'),
    path('edit/', authapp.edit, name='edit')

]
