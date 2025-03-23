from django.shortcuts import render
from django.http import HttpResponseRedirect # Função que redireciona o usuário para uma página específica
from django.urls import reverse # Função que gera URLs a partir de padrões de URL e parâmetros
from django.contrib.auth import logout, login, authenticate # Função de logout do Django
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """Encerra a sessão do usuário."""
    logout(request) # Django fornece uma função de logout que podemos chamar
    return HttpResponseRedirect(reverse('index')) # Redireciona o usuário para a página inicial do site

def register(request):
    """Faz o cadastro de um novo usuário."""
    if request.method != 'POST':
        # Exibe o formulário de cadastro em branco
        form = UserCreationForm()
    else:
        # Processa o formulário preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Faz login do usuário e o redireciona para a página inicial
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
        
    context = {'form': form}
    return render(request, 'users/register.html', context)