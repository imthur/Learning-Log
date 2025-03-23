from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model): # Define um modelo/tabela chamado Topic
    """Um tópico sobre o qual o usuário está aprendendo."""
    text = models.CharField(max_length=200) # Define um campo de texto com no máximo 200 caracteres
    date_added = models.DateTimeField(auto_now_add=True) # Define um campo de data e hora que armazena a data e hora atuais
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'topics' # Define o plural de 'Topic' como 'topics', passando essa informação para que o Django não adicione um 's' ao final do nome da tabela
        
    def __str__(self):
        """Retonar uma representação em string do modelo"""
        return self.text # Retorna o texto do campo text

class Entry(models.Model):
    """Algo específico aprendido sobre um tópico."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # Define um campo que estabelece uma relação entre as tabelas Topic e Entry
    text = models.TextField() # Define um campo de texto
    date_added = models.DateTimeField(auto_now_add=True) # Define um campo de data e hora, automaticamente preenchido com a data e hora atuais do momento da criação do objeto

    class Meta:
        verbose_name_plural = 'entries' # Define o plural de 'Entry' como 'entries', passando essa informação para que o Django não adicione um 's' ao final do nome da tabela

    def __str__(self):
        """Retorna uma representação em string do modelo"""
        return f"{self.text[:50]}..." # Retorna os primeiros 50 caracteres do campo text, seguidos de reticências

