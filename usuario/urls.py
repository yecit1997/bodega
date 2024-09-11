from django.urls import path
from django.contrib.auth import views as auth_views

from usuario import views


urlpatterns = [
    path('', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('admin_user/', views.admin_user, name='admin_user'),
    path('editar_usuario/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('editar_perfil/<int:id>/', views.editar_perfil, name='editar_perfil'),
    # path('cambio_contrasena/<int:id>/', views.editar_perfil, name='cambio_contrasena'),
    path('cambiar_contrasena/', auth_views.PasswordChangeView.as_view(), name='cambiar_contrasena'),
    path('cambiar_contrasena/done/', auth_views.PasswordChangeDoneView.as_view(), name='cambiar_contrasena_hecho'),
]
