from django.urls import path
from eapp import views

urlpatterns = [
    path('',views.index),
    path('udash',views.dashboard),
    path('admin_udash',views.admin_udash),
    path('view_product/<rid>',views.view_product),
    path('add_product',views.add_product),
    path('add_user',views.add_user),
    path('delete/<rid>',views.delete),
    path('remove/<rid>',views.remove),
    path('edit/<rid>',views.edit),
    path('register',views.register),
    path('login',views.user_login),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
]