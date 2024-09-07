from django.urls import path

from usuario import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('crear_superusuario/', views.crear_superusuario, name='crear_superusuario'),
]
