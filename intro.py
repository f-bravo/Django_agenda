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


