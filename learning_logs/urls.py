from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Define a URL padrão para o app learning_logs
    path('topics/', views.topics, name='topics'), # Define a URL para a página topics.html
    path('topics/<topic_id>/', views.topic, name='topic'), # Define a URL para a página topic.html, passando o argumento topic_id para a view topic
    path('new_topic', views.new_topic, name='new_topic'), # Define a URL para a página new_topic.html
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'), # Define a URL para a página new_entry.html, passando o argumento topic_id para a view new_entry
    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'), # Define a URL para a página edit_entry.html, passando o argumento entry_id para a view edit_entry
]