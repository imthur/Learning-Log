from django.apps import AppConfig # Importa a classe AppConfig do módulo apps do Django

class LearningLogsConfig(AppConfig): # Define a classe LearningLogsConfig, que herda de AppConfig
    default_auto_field = 'django.db.models.BigAutoField' # Define o campo de chave primária, setado por padrão como 'django.db.models.BigAutoField'
    name = 'learning_logs' # Define o nome do app como 'learning_logs'
