from django.urls import path

from producto import views

urlpatterns = [
    path('', views.productos, name='productos'),
    path('lista_tipos/<str:nombre_tipo>/', views.lista_tipos, name='lista_tipos'),
    path('estantes/', views.estantes, name='estantes'),
    path('ver_contenido_de_estantes/<int:id>/', views.ver_contenido_de_estantes, name='ver_contenido_de_estantes'),
    path('registrar_producto/', views.registrar_producto, name='registrar_producto'),
    path('detalle/<int:id>/', views.detalle, name='detalle'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
]



