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

"""
# Iniciando o GIT
# -> git init
OBS: usar o mesmo nome e email do GITHUB
# Criando nome de usuário:
-> git config --global user.name 'nome'
# Configurando email:
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

# Agora na página de contatos da para visualizar com nome e sobrenome

# além de criar a função __str__ no models também pode trabalhar na área admin
# colocando algumas configurações úteis 


# --------------------------------------------------------------------

# 454 - Customizando admin.ModelAdmin

# Colocando um list_display

# Não use o mesmo campo em list_editable e list_display_links.
# Gera um erro pois não pode adicionar um link em um input.


"""
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', # campos visíveis
    ordering = '-id',   # ordenação - é comum começar pelo último add       
    # list_filter = 'created_date',    # cria um campo para pesquisar por data
    search_fields = 'id', 'first_name', 'last_name'    # campo de busca
    list_per_page = 10    # número de contatos por página
    list_max_show_all = 200    # número máximo padrão a ser mostrado por página
    list_editable = 'first_name', 'last_name',    # deixa editar na área admin
    list_display_links = 'id', 'phone'    #  link q vai p/ página Modificar contact

"""


# ---------------------------------------------------------------------------------

# 455 - CRUD no django shell interativo e modelContact


# O model é craido apra trabalhar com dados - para n ter que digitar sql no django

# django shell interativo - é igual ao terminal do Python
# -> python manage.py shell
"""
from contact.models import Contact
>>> Contact
<class 'contact.models.Contact'>

# No Shell do Django ele não consegue checar algumas coisas pois n tem o formulário 
django. Exemplo: blank=True

c = Contact(first_name='Gustavo')

# O contato foi criado apenas na memória. Para salvar na base de dados digite:
c.save() 

# Acrescentando sobrenome ao c = 'Gustavo':
c.last_name = 'Moreira'
c.save()

c.phone = '475960473'

# para deletar: c.delete() 
# (1, {'contact.Contact': 1})

# Mesmo deletando fica na memória do Shell do Django.
# Se der um c.save() ele salva novamente, Tenha cuidado

# Dentro do Model do Django tem o object - que é o manage. Esse objetcs permite fazer
muitas coisas.
Pegando um Contato e editando com objects:
c = Contact.objects.get(id='4')
>>> c.first_name = 'Helena'
>>> c.save()
>>> c
<Contact: Helena Moreira>

>>> c = Contact.objects.all()
>>> c
<QuerySet [<Contact: João Oliveira>, <Contact: Luiz Machado>, <Contact: Helena Moreira>]>

>>> for contato in c: contato.first_name
... 
'João'
'Luiz'
'Helena'
>>>

# O que mais vai ser mais usado é o filter - mas ainda não tem nenhum filtro que é
a QuesrySet

>>> c = Contact.objects.filter(id=4)>>> c
<QuerySet [<Contact: Helena Moreira>]>

>>> c = Contact.objects.all().order_by('-id')
>>> c
<QuerySet [<Contact: Helena Moreira>, <Contact: Luiz Machado>, <Contact: João Oliveira>]>

# Usando o create - não precisa de save() pois ele salva direto na base de dados (não lazy)

>>> c = Contact.objects.create(first_name='Edu', last_name='Vieira')
>>> c
<Contact: Edu Vieira>


"""
"""
No Django as QuerySets a maioria delas serão (lazy), não vão na base de dados até que
puxe o valor. Precisa fazer um print ou um for na consulta por exemplo.
Isso permite fazer encadeamento de chamadas sem ficar indo na base de dados toda hora.
Faz o encadeamento e quando solitar os valores ai sim vai na base de dados.
"""


# ----------------------------------------------------------------------------------


# 456 - Criando ImageField e configurando MEDIA_URL e MEDIA_ROOT no settigns.py


# category - será outro campo e outro model que terá uma chave estrangeira 
"""
Nesse APP não vai precisar ter uma categoria para criar um contato.
Mas na maioria dos casos ao trabalhar com foreign key é comum primeiro ter que criar
a categoria e só depois criar o contato pois precisa da cageria salva na base de dados
para atrelar no campo da categoria do contato por exemplo.
"""

# category (foreign key) e show (boolean), picture (imagem)

# show = models.BooleanField(default=True)
# se n falar nada já vai cadastrar o contato mostrando.

# picture (imagem)
# a base de dados não vai ter o arquivo. Terá um link apontando para o arquivo.
# isso é mais performático. Salvar imagens na base de dados não é recomendado

# No contact/settings.py precisa registrar
# não vem por padrão no Django
# MEDIA_URL = 'media/'
# são arquivos que serão enviados pelo usuário

# precisa também colocar o media_root que coleta os arquivos enviados pelo usuário
# MEDIA_ROOT = BASE_DIR / 'media'


# pasta que coleta arquivos estáticos. pasta essa craida na raiz do site
# Caminho configurado no contact/settings.py
# STATIC_ROOT = BASE_DIR / 'static'  # collectstatic
# Esse collect static vai pegar todos arquivos estáticos e mover tudo para dentro da
# pasta static - e quando for configurar no servidor - diz onde ele vai buscar os
# arquivos estáticos que será na pasta 'static'

# Fazendo o collectstatic p n enviar p o github
# -> python manage.py collectstatic
# 126 static files copied to 'C:\Django_agenda\static'.                                

# precisa colotar os estáticos para garantir que não está usando coisas de dentro
# do projeto - mas já está usando os negócios de produção.

# no gitignore acrescente a pasta static/ para nao ir p github

# picture = models.ImageField(blank=True, upload_to='picture/%Y/%m')
# blank=True: para não ter que forçar enviar uma imagem
# upload_to='picture/%Y/%m' cria uma pasta (picture) dentro da pasta media e dentro
# da pasta picture cria cria outra pasta do ano atual e dentro do ano cria do mês atual

# Faça as migrações 
# python manage.py makemigrations

# deu um erro
"""
SystemCheckError: System check identified some issues:

ERRORS:
contact.Contact.picture: (fields.E210) Cannot 
use ImageField because Pillow is not installed
"""

# deu esse erro pois foi buscado um campo imageField
# Mas o Django depende do Pillow para trabalhar com essas imagens.
# python -m pip install Pillow
# com o pillow instalado agora as migrações serrão enviadas
"""
python manage.py makemigrations     
Migrations for 'contact':
  contact\migrations\0002_contact_picture_contact_show.py       
    - Add field picture to contact
    - Add field show to contact
"""

# outro erro:
"""
You have 1 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): contact.
Run 'python manage.py migrate' to apply them.
"""
# Não foi aplicado o contact.show 
# Não deu certo pois o comando: python manage.py makemigrations     
# makemigrations - cria os arquivos de migração mas quem migra é o:
# -> python manage.py migrate
"""
manage.py migrate        
Operations to perform:
  Apply all migrations: admin, auth, contact, contenttypes, 
sessions
Running migrations:
  Applying contact.0002_contact_picture_contact_show... OK  
"""
# Basta atualizar que volta a funcionar.

# agora os campos Show e Escolher um arquivo estão disponíveis.

# Se tentar abrir o link do arquivo não vai funcionar.
# O django tenta usar o MEDIA_URL = 'media' do settings.py
# O django não configura isso.
# Se em desenvolvimento deseja trabalhar com a MEDIA dessa maneira precisa configurar
# a URLS do projeto para que consiga servir as imagens.
# Em produção quem serve é o servidor.

# Vá na urls.py do projeto
# import:
# from django.conf.urls.static import static
# Agora precisa fazer uma importação específica para importar do SETTINGS:
# from django.conf import settings
# agora na importação do settings tem tudo que tem no settings do django
# -> urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# -------------------------------------------------------------------


# 457 - Criação do Model Caregory e ligação com Contact por FK


# Poderá ser criada um contato sem categoria

# Será criado uma class no contact/models.py
"""
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name

Adicionando um campo na tabela Contact para fazer a PK
# category = models.ForeignKey(Category, on_delete=models.SET_NULL, )

on_delete SET_NULL - ao apagar a category o contato linkado nela ficará nulo.
Com isso precisa deixar que no contato criado a categoria possa ser nula - blank=True
e permitir que o valor seja nulo. null=True
"""

# Fazendo as migrações:
# -> python manage.py makemigrations
"""
Migrations for 'contact':
  contact\migrations\0003_category_contact_category.py
    - Create model Category
    - Add field category to contact
"""
# -> python manage.py migrate
"""
Operations to perform:
  Apply all migrations: admin, auth, contact, contenttypes, sessions
Running migrations:
  Applying contact.0003_category_contact_category... OK
"""

# Agora registre a Category em contact/admin.py
"""
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
"""

# Agora na área adimin foi criada a categoria e pode adicionar contatos a ela.


# ------------------------------------------------------------------------------


# Corrigindo o nome errado 'Categorys'

# No Django - model meta options - uam classe dentro de outra classe
"""
https://docs.djangoproject.com/en/4.2/ref/models/fields/

Cria uma classe dentro do model chamada Meta
- verbose_name - versão humana de leitura para o model
- verbose_name_plural
# Sempre que o Django solicitar o model ele vai usar o verbose_name da classe meta

O Django criou Contacts corretamente e Categorys ele errou

# Configurando a classe meta: configura metadados dos dados
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
"""


# -------------------------------------------------------------------------------


# 459 - Criando o campo owner - usando o model User do Django

# Colocando uma PK de owner no Contact:
"""
Para quando for criar os templates e as views, o usuário que criou o contato, tenha
permisão de editar, apagar, etc. O contato é de quem criou por isso owner.
O django já tem um sistema de usuários. Se estiver criando algo que nã oseja tão 
complexo, pode usar o próprio seitema de autenticação Django.

Se precisar colocar mais campos o ideial é que extenda o usuário com outro model.
Por exemplo criaria outro model onde tem os dados do perfil do usuário, uma bio ou 
uma foto ao invés de editar o próprio model existente
"""
# No shell do Django:
# -> python manage.py shell
# from django.contrib.auth.models import User

# O user é modo padrão de usuários do Django - pode usar para criar, obter, etc.
# Criando usuário - coloque numa variável.
# o create_user() - precisa ser assim pois já faz a criptografia
# -> user = User.objects.create_user(username='XXX', password='XXX')
# com esse comando não precisa de user.save()

# feito isso criou um user com username e senha que é suficiente para poder logar 
# nessa área
# O usuário criado não tem staff account marcado. Com isso o usuário não consegue
# logar na área Django Administration.
# Sendo assim ,pode usar esse usuári odo Django sem correr o risco de alguém logar 
# na área adiminstrativa do Django.

# No site - terá a opção para que as pessoas possam criar contas.
# Esses usuários não terão staff account nem super users staff marcadas.
# As pessoas vão conseguir logar na área que será criada e destinada a isso.
# Ai começa a trabalhar com permissões - se determinado usuário pode ou não editar
# determinado contado baseado se ele é ou não owner, se foi ele que criou ou não.

# seguindo...
# Criando em contact/models.py class Contact() o owner
"""
 owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
"""
# Modificou o models faça as migrações.
# -> python manage.py makemigrations
"""
contact\migrations\0004_alter_category_options_contact_owner.py
  - Change Meta options on category  <- feita antes 
  - Add field owner to contact
"""
# -> python manage.py migrate

# Agora ao criar um contato da para selecionar quem vai ser o owner

# vamos usar uma lib externa - faker - para popular o banco com dados aleatórios
# para desenvolver o frontend


# --------------------------------------------------------------------------------


# colocando no topo do arquivo para não ver mais os erros de tipagem e pep8
# type: ignore
# flake8: noqa


# 460 - Gerando dados no Django com Faker

# criando uma pasta na raiz com o arquivo create_contacts.py
# utils/create_contacts.py

# O script está explicado
# como não precisa do manage.py o comando será:
#-> python utils/create_contacts.py


# ------------------------------------------------------------------------------


# 461 -Usando local_settings para sobrescrever variáveis de settings


"""
Muitas settings que vem por padrão no Django terão que ser mudada.
Isso gera incompatibilidade se tiver usando algo como Git. Pois terá um arquivo de
settings e terá dados diferentes quando for usar o computador local e no servidor.
E isso pode gerar transtornos.
Existem algumas táticas para pegar essas configurações do settings.py dinamicamente.
Por exemplo, utilziar o .env - para Django .env
A lógica é:
Cada local que for utilziar o proejto seja local ou servidor, será criado um arquivo
que não será monitorado pelo git. Geralemten de nome local_settings.py.

No settings lá no final. Não pode ter nada depois pois pode dar problema.
colque um try para tentar improtar o módulo
try: 
    from project.local_settings import *
except ImportError:
Agora qualquer coisa que for colocada nesse arquivo, que não vai está no github,
estará disponível apenas no local que estiver nesse caso só no seu computador.
Por exemplo se sobrescrever qualquer configuração do settings.py já vai funcionar.

# É uma tática para ter settings baseada no local que estiver seja no servidor ou local
# é uam tática para contornar o problema de settings diferentes p cada ambiente
"""
# Colocando o caminho do local_settings no gitignore para n ser trackeado
# lá no servidor esse arquivo tem que ser criado manualmente


# --------------------------------------------------------------------


# 462 - Organizando view.py num packeage sem quebrar código

"""
# O view é um módulo padrão sugerido pelo Django para organização.
E para não sair desse padrão módulos Python da para "enganar" criando um pacote 
Python de mesmo nome para utilizar como se fosse um módulo utilizando o arquivo
__init__.py do package. Oinit é executado quando improta o package.
Crie um package chamada views no APP
Crie um arquivo chamdo __init__.py
O __init__ além de indicar que é um módulo python, ele indica quando o package for
importado ele é a primeira coisa a ser executada.
Para organizar será criado packages dentro da pasta views.
Se qualquer arquivo ficar muito grande pode fazer essa tática para separar eles.
Você precisa simular que o package viewa é o arquivo views.py padrão do Django

# Copie o código que está no arquivo views.py, cole no novo arquivo criado criado
contact_views.py e exclua o views.py do Django
OBS: normalmente não é recomendado excluir algo sem que já esteja funcionando mas
nesse caso não tem alternativa pois não da para ter um package e um arquivo de fora 
com o mesmo nome.
# isso vai gerar um problema pois em urls.py o import precisa ser mudado.
Como o __init__.py é a priemira coisa a ser executada, os imports vão paracer que
estão vidno direto do package views
Então no __init__.py: faça o import do arquivo contact_views.py
from . contact_views import *
"""
# Essa a maneira de "enganar" o django.
# É como se o package views fosse o módulo views.py só porque no __init__ é importado
# tudo de dentro que será criado apra ficar mais organizado

# Tenha atenção agora pois toda vez que criar um novo arquivo no package views precisa
# fazer as importações no __init__.py. Se esquecer de fazer isso os arquivos criados
# para views não serão importados
# Outra obs é que o flake8 fica dando erro dizendo que não está utilizando.
# Como não terá nenhuma lógica coloque no arquivo __init__.py: # flake8: noqa










