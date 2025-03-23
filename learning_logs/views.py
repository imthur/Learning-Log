from django.shortcuts import render # Importa a função render
from .models import Topic, Entry # Importa o modelo Topic do arquivo models.py
from .forms import TopicForm, EntryForm # Importa o formulário TopicForm do arquivo forms.py
from django.http import HttpResponseRedirect # Importa a função HttpResponseRedirect
from django.urls import reverse # Importa a função reverse

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html') # Renderiza a página index.html

def topics(request):
    """Mostra todos os tópicos."""
    topics = Topic.objects.order_by('date_added') # Busca todos os objetos Topic e os ordena por data de criação / Topic é um modelo/tabela do banco de dados, criado em models.py
    context = {'topics' : topics} # Cria um dicionário com a chave 'topics' e o valor topics, que contém todos os objetos da tabela Topic
    return render(request, 'learning_logs/topics.html', context) # Renderiza a página topics.html, passando o dicionário context [criado acima] como argumento

def topic(request, topic_id):
    """Mostra um único tópico e todas as suas entradas."""
    topic = Topic.objects.get(id=topic_id) # Busca um objeto Topic com o id passado como argumento
    entries = topic.entry_set.order_by('-date_added') # Busca todas as entradas relacionadas ao tópico e as ordena pela data de criação
    context = {'topic': topic, 'entries': entries} # Cria um dicionário com as chaves 'topic' e 'entries' e os valores topic e entries, respectivamente
    return render(request, 'learning_logs/topic.html', context) # Renderiza a página topic.html, passando o dicionário context como argumento

def new_topic(request):
    """Adiciona um novo tópico."""
    if request.method != 'POST': # Se a requisição não for do tipo POST
        # Nenhum dado submetido; cria um formulário em branco
        form = TopicForm() # Cria um formulário vazio
    else:
        # Dados de POST submetidos; processa os dados
        form = TopicForm(data=request.POST) # Cria um formulário preenchido com os dados submetidos
        if form.is_valid(): # Se o formulário for válido
            form.save() # Salva os dados do formulário no banco de dados
            return HttpResponseRedirect(reverse('topics')) # Redireciona o usuário para a página topics.html, usando a função reverse para obter a URL de topics

    context = {'form': form} # Cria um dicionário com a chave 'form' e o valor form, que contém o formulário
    return render(request, 'learning_logs/new_topic.html', context) # Renderiza a página new_topic.html, passando o dicionário context como argumento

def new_entry(request, topic_id):
    """Adiciona uma nova entrada para um tópico em particular."""
    topic = Topic.objects.get(id=topic_id) # Busca um objeto Topic com o id passado como argumento
    if request.method != 'POST': # Se a requisição não for do tipo POST
        # Nenhum dado submetido; cria um formulário em branco
        form = EntryForm() # Cria um formulário vazio
    else:
        # Dados de POST submetidos; processa os dados
        form = EntryForm(data=request.POST) # Cria um formulário preenchido com os dados submetidos
        if form.is_valid(): # Se o formulário for válido
            new_entry = form.save(commit=False) # Salva os dados do formulário no banco de dados, mas não o commita
            new_entry.topic = topic # Define o campo topic do objeto new_entry como o objeto topic
            new_entry.save() # Commita as alterações no banco de dados
            return HttpResponseRedirect(reverse('topic', args=[topic_id])) # Redireciona o usuário para a página topic.html, passando o argumento topic_id

    context = {'topic': topic, 'form': form} # Cria um dicionário com as chaves 'topic' e 'form' e os valores topic e form, respectivamente
    return render(request, 'learning_logs/new_entry.html', context) # Renderiza a página new_entry.html, passando o dicionário context como argumento
    
def edit_entry(request, entry_id):
    """Edita uma entrada existente."""
    entry = Entry.objects.get(id=entry_id) # Busca um objeto Entry com o id passado como argumento
    topic = Entry.topic # Busca o tópico relacionado à entrada
    if request.method != 'POST': # Se a requisição não for do tipo POST
        # Requisição inicial; preenche o formulário com a entrada atual
        form = EntryForm(instance=entry) # Cria um formulário preenchido com os dados da entrada
    else:
        # Dados de POST submetidos; processa os dados
        form = EntryForm(instance=entry, data=request.POST) # Cria um formulário preenchido com os dados submetidos
        if form.is_valid(): # Se o formulário for válido
            form.save() # Salva os dados do formulário no banco de dados
            return HttpResponseRedirect(reverse('topic', args=[topic.id])) # Redireciona o usuário para a página topic.html, passando o argumento topic.id

    context = {'entry': entry, 'topic': topic, 'form': form} # Cria um dicionário com as chaves 'entry', 'topic' e 'form' e os valores entry, topic e form, respectivamente
    return render(request, 'learning_logs/edit_entry.html', context) # Renderiza a página edit_entry.html, passando o dicionário context como argumento