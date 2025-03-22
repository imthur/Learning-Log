from django.contrib import admin # Importa o módulo admin
from learning_logs.models import Topic, Entry # Importa os modelos Topic e Entry do arquivo models.py

admin.site.register(Topic) # Registra o modelo Topic no site de administração
admin.site.register(Entry) # Registra o modelo Entry no site de administração