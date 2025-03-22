from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm): # Define um formulário para o modelo Topic, que é um campo de texto
    class Meta: # Define uma classe Meta para o formulário
        model = Topic # Define o modelo que o formulário representa
        fields = ['text'] # Define os campos que o formulário deve exibir
        labels = {'text': ''} # Define um rótulo para o campo text

class EntryForm(forms.ModelForm): # Define um formulário para o modelo Entry, que é um campo de texto
    class Meta: # Define uma classe Meta para o formulário
        model = Entry # Define o modelo que o formulário representa
        fields = ['text'] # Define os campos que o formulário deve exibir
        labels = {'text': ''} # Define um rótulo para o campo text
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # Define um widget para o campo text, que é um campo de texto grande com 80 colunas
