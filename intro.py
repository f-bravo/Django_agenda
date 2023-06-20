# Comandos:

# ------------------------------------------------------

"""
# Iniciando o projeto: 
# Criando o ambiente virtual:
-> python -m venv venv
# Ativando oambiente virtual no Windows 
-> . venv\Scripts\Activate
# instalando o django
-> pip install django
# Atualizar o pip
-> pip install --upgrade pip
# Startando o project
-> django-admin startproject project .
Teste para ver se o django está ok. Se n tiver feche e abra o VSCode
-> python manage.py runserver
"""

#--------------------------------------------------------
# Configurando o git ignore --> arquivos que não vão para o respositório
"""
crei o .gitignore na raiz do projeto 
busque no google --> django gitignore 
https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/
Cole os comandos dentro da pasta .gitignore
"""

# Baixe o GIT - aplique as opção default

"""
OBS: usar o mesmo nome e email do GITHUB
# Criando nome de usuário:
-> git config --global user.name 'nome'
# Configurando email - outlook.com
-> git config --global user.email 'email@email.com'
# Olhando as configurações do GIT:
-> git config --global

# Eu não alterei 0 defaultBranch para main - deixei como master
# estava dando erro na hora de dar o push

# Adicioanando:
-> git add .  - para adicionar tudo

# Dando o primeiro Commit
-> git commit -m 'intro1'

# dando um git log - para ver o que foi feito:
# ou git log --oneline
# R: c5ef3d1 (HEAD -> master) Initial

# Crei o repositório no perfil do github
Adicionando o repositório remoto: 
copie a chave https e dê o seguinte comando:
-> git remote add origin https://github.com/f-bravo/Django_agenda.git

# Enviando os commites: 
-> git push origin master

# digite usuário e senha e pronto - será enviado

#------------------------------------------------------

# Sempre que modificar um arquivo ou vários tem que repetir o processo:

-> git add . (ou) git add nome_do_arquivo
-> git commit -m 'explicação'
-> git push origin master
# ------------------------------------------------------------

# OBS na próxima vez pode setar (-u) o nome para digitar apenas git push:
-> git push origin master -u

"""

#--------------------------------------------------------------------
# - 447
# --------------------------------------------------------------------


# criando o APP contact
# python manage.py startapp contact

# Sempre que criar um APP:
# Vá em projetc/settings na lista INSTALLED_APPS = [..., contact1, ]


#---------------------------------------------------------------------------------
# - 448 - criando e configurando as pastas base_templates e base_static
# --------------------------------------------------------------------------------


# crie a name_space global dentro das pastas criadas.

# Dica: para criar as pastas e os arquivos de uma vez só. New file:
# base_static/globa/css/style.css

# Configurado as pastas: coloque o caminho em project/settings 
# TEMPLATES = [
#       'DIRS': [BASE_DIR / 'base_templates'], ]

# Static FILES:
# STATICFILES_DIRS = ()


# Criando a pasta templates no APP contact com o nome_space do APP + index.html, a home

# Criando um arquivo no APP contact - urls.py
"""
from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index' ),
]
"""   
# Em contact/views:
"""
def index(request):
    return render(
        request,
        'contact/index.html',
    )
"""

# Agora vá project/urls.py para referenciar 
# path('', include('contact.urls')),
# Esse caminho vazio vai buscar a urls.py de contact que vai carregar o index
#   é como se a raiz do site estivesse aqui: path('', views.index, name='index' )

# Ta sem nenhuma URL - porque foi passado uma url vazia na url principal
# e pegar a urls vazia novamente em contac.

"""
git add . 
-> git commit -m 'Criando App contact, base_templates e base_static'
-> git push origin master -u
"""


# -----------------------------------------------------------------
# Criando e editando a senha de um super usuário Django
# -----------------------------------------------------------------


# Django trabalha com migrations
# sempre que quiser replicar tudo que já foi feito, terá um passo a passo
# para fazer e desfazer 
# As migrações não foram aplicadas e as tabelas não foram criadas no db.sqlite3 

# As migrações foram criadas. 
# Nesse momento o único comando que precisa é:
# -> python manage.py migrate
"""
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
"""
# Ao criar o model, os arquivos de migration também vão ser mostrados

# Após aplicar as migration suba o servidor.
# vá na uls e coloque /admin para abrir a parte de administração

# Criando o super user
# o super user tem acesso a quase tudo na base de dados do Django incluindo
# a parte administratica.
# -> python manage.py createsuperuser
# escolha usuário, e-mail e senha. Confirme a senha e pronto.
# Superuser created successfully.

# Caso esqueça a senha:
# -> python manage.py changepassword USER_NAME

# É recomendado que não altere o validor de senha padrão do Django
# que já vem configurado. 


# -------------------------------------------------------------------

# 451 - Base de dados, tabelas e documentação:

# por padrão o Django vem com SQLite. 
# O SQLite não é base de dados para trablahr em produção com sites
# Mas só no final quando for passar esse servidor para um real
#   no project/settings DATABASES = {...}

# depois de aplicar as migrates da para ver as tabelas do sqlite3


# --------------------------------------------------------------------

# 452 - Django Models - model

# No app contact/models.py:

# A class Model Será usada para criar, buscar, atualizar e deletar contatos
# Esse model vai geratar uma nova migração - vamos migrar para criar a tabela
# na base de dados
# Todos os campos criados no model são obrigatórios.
# Se quiser colocar campo opcional coloque no final - blank=True 
"""
--> charfield no django precisa passar o tamanho máximo
--> created_date será usado o módulo para criar automático a data e hora da criação
TIME_ZONE = 'America/Sao_Paulo' --> modificado no project/settings
"""

# sempre que fizer editar o models precisa executar o comando:
# -> python manage.py makemigrations 
"""
Com isso o django vai criar uma migração da class Contact e quando for aplicar
as migrações ele vai salvar tudo na base de dados criando as tabelas e os campos.
"""
# O arquivo foi criado em migrations
# é muito raro editar uma migração no próprio arquivo.
# geralmente vai editar as tabelas na base de dados criando novas migraçoes p fazer 
# as edições.

# faça a migração.
# -> python manage.py migrate 
# Operations to perform:
#   Apply all migrations: admin, auth, contact, contenttypes, sessions
# Running migrations:
#   Applying contact.0001_initial... OK


# -------------------------------------------------------------------

# 453 - Registrando o model na área administrativa em admin.py e register

# precisa rigistrar o model em contact/admin.py
# O padrão será nome_do_modelAdmin()
# Essa classe criada é como uma configuração na admin do django
# precisa fazer a importação: from contact import models

# feito isso na área de admin do django já mostra contacts
# ao adicionar contact da p ver um formulário.
# campos em negrito são os obrigatórios 

#OBS: os blank trabalha no formula´rio do Django e não na base de dados

# Criado o primeiro contato ele mostra como - Contact object (1)
# para que não seja exibido assim crie uma função __str__ no model Contact









