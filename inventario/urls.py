from django.urls import path

from inventario import views

urlpatterns = [
    path('', views.inventario, name='inventario'),
    
]



