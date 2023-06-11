from django.urls import path

from . import views

urlpatterns = [
    path('cadastro/',views.cadastro, name="cadastro"),
    path('login/',views.login, name="login"),
    path('index/', views.index, name="index"),
    path('user/', views.user, name='usuario')
]