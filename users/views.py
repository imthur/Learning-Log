from django.http import HttpResponseRedirect # Função que redireciona o usuário para uma página específica
from django.urls import reverse # Função que gera URLs a partir de padrões de URL e parâmetros
from django.contrib.auth import logout # Função de logout do Django

def logout_view(request):
    """Encerra a sessão do usuário."""
    logout(request) # Django fornece uma função de logout que podemos chamar
    return HttpResponseRedirect(reverse('index')) # Redireciona o usuário para a página inicial do site