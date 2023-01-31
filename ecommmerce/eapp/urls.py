from django.urls import path
from eapp import views

urlpatterns = [
    path('',views.index),
    path('udash',views.dashboard),
    path('view_product/<rid>',views.view_product),
    path('add_product',views.add_product),
    path('delete/<rid>',views.delete),
    path('register',views.register),
    path('login',views.user_login),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
]