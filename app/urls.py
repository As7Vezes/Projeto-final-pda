from django.urls import path

from app import views

urlpatterns = [
    path('',views.index, name="home"),
    path('sobre/',views.sobre, name="sobre"),
    path('contato/',views.contato, name="contato"),
]