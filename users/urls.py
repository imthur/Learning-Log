from django.urls import path # Importa a função path
from django.contrib.auth import views as auth_views # Importa as views de autenticação do Django
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), # Django fornece uma função de login que podemos chamar
    path('logout/', views.logout_view, name='logout'), # Django fornece uma função de logout que podemos chamar
]