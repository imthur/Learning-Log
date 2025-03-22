from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Define a URL padrão para o app learning_logs
    path('topics/', views.topics, name='topics'), # Define a URL para a página topics.html
    path('topics/<topic_id>/', views.topic, name='topic'), # Define a URL para a página topic.html, passando o argumento topic_id para a view topic
    path('new_topic', views.new_topic, name='new_topic'), # Define a URL para a página new_topic.html
]