# Learning Log

## 📌 Sobre o Projeto
O **Learning Logs** é um projeto desenvolvido como parte dos meus estudos em Django. Ele é baseado no livro *Curso Intensivo de Python: uma Introdução Prática e Baseada em Projetos à Programação*.

O objetivo do Learning Logs é fornecer uma plataforma simples, mas funcional, onde os usuários possam registrar e acompanhar seus estudos. Cada usuário pode criar tópicos de aprendizado e adicionar entradas de anotação relacionadas, formando um histórico organizado do seu progresso.

## 🚀 Funcionalidades
- Cadastro e autenticação de usuários.
- Criação e gestão de tópicos de estudo.
- Adição de anotações relacionadas a cada tópico.
- Restrinção de acesso, garantindo que cada usuário visualize apenas seus próprios dados.

## 🛠️ Tecnologias Utilizadas
- **Django**: estruturação do back-end e lógica da aplicação.
- **SQLite**: banco de dados utilizado para armazenar as informações.
- **Django Authentication System**: sistema de autenticação e proteção de dados.
- **Bootstrap**: estilização responsiva e intuitiva da interface.
- **HTML e Django Templates**: renderização dinâmica dos dados.

## 📂 Estrutura do Projeto
```
learning_logs/
│── learning_logs/   # App principal
│   ├── settings.py  # Configurações do Django
│   ├── urls.py      # Rotas da aplicação
│   ├── models.py    # Modelagem do banco de dados
│   ├── views.py     # Lógica das requisições
│   ├── templates/   # Arquivos HTML
│   ├── static/      # Arquivos CSS e JS
│── db.sqlite3       # Banco de dados
│── manage.py        # Arquivo de gerenciamento do Django
```

## 🏁 Como Executar o Projeto
### 1️⃣ Clonar o repositório
```sh
git clone https://github.com/imthur/Django-Learning.git
cd Django-Learning
```

### 2️⃣ Criar e ativar um ambiente virtual
```sh
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate     # Para Windows
```

### 3️⃣ Instalar as dependências
```sh
pip install -r requirements.txt
```

### 4️⃣ Executar as migrações e iniciar o servidor
```sh
python manage.py migrate
python manage.py runserver
```
Acesse a aplicação no navegador: `http://127.0.0.1:8000/`

## 📌 Considerações Finais
Este projeto foi um excelente exercício para compreender melhor os fundamentos do Django e do desenvolvimento web. Trabalhei desde a modelagem de dados até a implementação do front-end, consolidando conhecimentos essenciais para aplicações dinâmicas. 

📌 Repositório: [github.com/imthur/Django-Learning](https://github.com/imthur/Django-Learning.git)

Fique à vontade para explorar, testar e sugerir melhorias! 🚀
