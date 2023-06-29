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


# --------------------------------------------------------------------------------


# 463 - enviando o CSS


# --------------------------------------------------------------------------------


# 464 - injetando contatos dentro do contexto do template index.html


"""
Na página inicial a gente quer exibir os contatos e para isso precisa injetar os
contatos dentro da view index que está no package views/contact_views.py

Mas antes precisa organizar o BASE pra que ele bata com o CSS.
No CSS na classe .contet{} é a parte onde estão os contatos, o 'miolo' do site. É a 
parte principal da página, a (main).

No base templates/global/base.html precisa colocar o .content do CSS. 
Pode fazer de duas formas:
1 - criando um block de content
    {% block content %}{% endblock content %}
Com isso faria todo o body dentro de template/contact/index.html

2 - criar o content no base fora do bloco e no template/contact/index.html coloca o 
conteúdo do main.
# Coloque a TAG main com a class="content" no base_templates/global/base.html para
que exista em todas as páginas que extender o base.

Para injetar os contatos no templates/contact/index.html é utilizar na contact_view.py
o models para buscar os dados do contatos.
"""
# Em contact_views.py:
"""
from django.shortcuts import render
from contact.models import Contact

def index(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts,
    }
    return render(
        request,
        'contact/index.html',
        context
    )"""


# ---------------------------------------------------------------------------------


# 465 - Criando tabela que exibe os contatos no index.html


# ---------------------------------------------------------------------------------


"""
Por ser uma tabela ela não pode ser quebrada em outra linha. A tabela só encolhe e
expande.
Então foi criada uma  div no CSS chamada e .responsive-table{}
Essa classe não permite que a tabela passe p fora do conteúdo da página
É uma tática para fazer uma tabela rasponsiva.
no celular vai poder arrastar a barra para os lados
"""
# O código está no index.html 
# tabela: <table>
# título: <caption
# Cabeçalho da tabela: <thead>
# Corpo da tabela: <tbody> com FOR para criar as linhas dos contatos com cada coluna
# preenchida com contact.nome_da_coluna


# -----------------------------------------------------------------------------


# 466 - Manipulando QuerysSets Django (filter, order_by e slice)


# no django admin tem a opção (show) para exibir um contato ou não. Se desmarcar 
# o contato nã oserá exibo. É preciso corrigir isso com o filter

# no package views/contact_views.py: 
"""
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[0:10]
"""
# selecione todos os contatos onde show=True e ordene por -id decrescente
# vamos usar paginação - mas se tiver ruim ter que rolar a pagina para baixo ou 
# p cima use fatiamento. [0:10]

# se quiser ver as querys que estão sendo feita adicione o print abaixo.
# print(contacts.query)


# -------------------------------------------------------------------------------


# 467 - Criando template - view e a url par aexibir contato único.


# ao clicar no id do contato ir para p outra url - rederizar outro template p 
# mostrar um único contato
# vai precisar de uma url, um template e uma view para separar pois o index atual 
# é diferente do que quer exibir com apenas um contato.

# Primeira coisa: ir no contact/templates e criar um novo template contact.html
# cria-se primeiro o templete posi a view renderiza o template
# depois cria a view porque a URL depende da view

# Vai no contact.html o global/base.html
# {% extends 'global/base.html' %}

# Colocando as classes no block:
"""
{% block content %}
  <div class="single-contact">
    <h1 class="single-contact-name">
      {{ contact.first_name }} {{ contact.last_name}}
    </h1>    
  </div>  
{% endblock content %}
"""

# Agora na contact_views.py crie a view contact no singular:
# na busca será .get() que retorna um único valor
# o get vai receber uma pk. Será recebido na url - a url vai enviar um contact_id
"""
def contact(request, contact_id):
    single_contact = Contact.objects.get(pk=contact_id)

    context = {
        'contact': single_contact,
    }
    return render(
        request,
        'contact/contact.html',
        context
    )
"""

# Na URLS vai criar uma nova urls
# a url se contact, a view se chama contact - nomes iguais deixa consistente
# recendo um parâmetro dinâmico. <int:contact_id> esse nome está tbm na views
# path('<int:contact_id>/', views.index, name='contact'), não esqueça / na url
"""
urlpatterns = [
    path('<int:contact_id>', views.index, name='contact'), # type:ignore
    path('', views.index, name='index'),  # type:ignore
]
"""
# As urls foram invertidas - mesmo com a recomendação de deixar as mais específicas
# para o final p não correr risco de dar mach com algo errado.

# Agora coloque os campos a serem exibidos na urls para o contact único:
"""
<p><b>ID: </b> {{ contact.id }}</p>
    <p><b>E-mail: </b> {{ contact.email }}</p>
    <p><b>Phone: </b> {{ contact.phone }}</p>
    <p><b>Created Date: </b> {{ contact.created_date }}</p>
    <p><b>Description: </b> {{ contact.description }}</p>
    <p><b>Category: </b> {{ contact.category }}</p>
"""

# Colocar links:
# ao clicar nos IDs da página de contatos será direcionado p/ o contato
# contact/contact mais parâmetro <int:contact_id>
# no index.html:
# <a class="table-link" href="{% url 'contact:contact' contact.id %}">

# o get() da view se ele não encontrar um valor ou encontrar mais de um valor 
# ele vai lançar um erro. Ele precisa encontrar um valor.
# A maneira mais simples de resolver isso é substituir o get por filter() usando 
# um last() ou first() valor
# veja abaixo a mudança de get para filter: 
"""
def contact(request, contact_id):
    single_contact = Contact.objects.filter(pk=contact_id).first()
"""

# mas agora cai em outro problema: 
# ele não da erro mas retorna a query vazia sem valores. 
# precisa importar e fazer um if na função
# from django.http import Http404
# if single_contact is None:
#   raise Http404()

# isso é tão comum de fazer que o Django tem um atalho:
# acrescente no import o get_list_or_404
# from django.shortcuts import get_list_or_404, render

"""
def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()    <-anterior
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
""" 
# Pode passar o contact que é o model e passar os filtros para dentro da função
# single_contact = get_object_or_404(Contact.filter(pk=contact_id, show=True))

# passar o manage somente
# single_contact = get_object_or_404(Contact.objects, pk=contact_id, show=True)

# passar somente o model
# single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

# É importante saber pois em alguns momentos precisa manipular a consulta para 
# fazer algo que a get_objetct_or_404 não faz 
# mas nesse momento não precisamos então não importa muito.

# tenha cuidado pois o mesmo  filtor que usa para oculatr coisas como o show
# desmarcado, tem que usar quando pfr buscar um contato único


# -----------------------------------------------------------------------------


# 468 - criando cabeçalho principal do site

"""
Classes do CSS - Header, header-deading, header-link, header-link:hover, menu, etc.

Vamos começar fazendo no base_templates/base.html e deposi tirar no partial
"""

# toda vez que clicar na Agenda do cabeçalho tem que ir para a home do site
# contact:index
# <a href="{% url 'contact:index' %}" class="header-link">

# <form action="" method="get"> 
# Todo formulário do tipo get vai atrelar o Search pesquisado lá na url


# ---------------------------------------------------------------------------------


# 469 - Criando arquivos parciais para usar com include nos templates


# Separando em parciais - separando a header.
# Tenha critério quando separa pois tem queda de performance e também fica confuso

# crie uma pasta partial no base_tempaltes/global/partial e crei o _header.html
# quando é um partial é costume colcoar um undeline na fretne do nome do arquivo

# onde estava o header no base.html coloque o include com o caminho do _header.html
#  {% include 'global/partials/_header.html' %}

# Lembrando: fazer o partials é bom para quando repete muito código html.
# Corte o código, coloque num partial e faça o include onde precisar repetir

# outra coisa boa de tirar é a head - depednedo do site fica muito grande e bagunçado
# - para não bagunçar o base inteiro, vou tirar o que está entre a TAG <head> e
# colocar no partials _head.html
"""
Isso gera un  transtorno pois onde está carregando o static tem que utilizar o load static
Inclua o {% load static %} no arquivo _head.html e também o caminho:
#  {% include 'global/partials/_head.html' %}

# adicione no contexto do título para mostrar que é o título do site
<title>{{ site_title }}Agenda</title>
# vá no package views/contact_views.py e em context adicione na def index(request):
o context {'site_title': 'Contatos - ' }

# na outra views coloqcar o nome do contato inteiro fica interessante]

em def contact crei a variável contact_name:
    site_title = f'{single_contact.first_name} {single_contact.last_name}'
e que tem o nome para o contato pode passar para o site_title no context da função
  'site_title': contact_name
"""

# Agora a página fica com o título + o nome do contato ao lado 


# ---------------------------------------------------------------------------------


# 470 - Filtrando valores com Q e OR para o campo de pesquisa


# melhorando a busca do search
# vamso renderizar a mesma coisa, vai usar o mesmo template...
# ainda sim é melhor trabalhar com uma nova views para nã odeixar ela com muitos if
# Caso necessário pode até criar um template
# Crie uma nova view em views/contact_views.py

# precisa ter uma url p/ atrelar no <form action="{% url 'contact:search' %}" method="GET">
# caminho criado na contact/urls.py
# path('<search/', views.search, name='search'), # type:ignore

# Agora está correto a ulr com o search/ e o parâmetro q=chave e o valor que é o teste
# http://127.0.0.1:8000/%3Csearch/?q=teste
# Essa chave é o name do form

# Na views:
# search_value = request.GET.get('q', '').strip() 
# utilize o método get passando a chave e não tiver nada a string vazia para ndar erro 
# quando não vier nada. O strip() remove espaço do começo e do fim.
# O strip limpa limpa um pouco a consulta

# Não quero que o usuáio envie um monte de valores vazios pois o servidor aceita 
# Caso o usuário digite um valor vazio ou não mande o (q) vou redirecioanr para o index
# para tirar o usuário da url search odne tava tentando buscar algo que não foi enviado
# para isso use um atalho nos imperts chamado redirect
# acrescente o IF abaixo p checar se o valor foi enviado. Se não foi redireciona p home
# if search_value == '':
#   return redirect('contact:index')
# Se o usuário apenas der enter volta direto para a home

# Para checar se o campo contém o trech oque a pessoa ta buscando
# https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups

# Para utilizar filtros lookups:
# Foi acrescentado outro filtro.
# Pegue o nome que foi escolhido e coloque na frente no campo que está buscando.
# .filter(first_name__icontains=search_value)\
# agora chega o trecho do que estiver sendo buscado.
# A letra (i) de icontains é para não diferenciar maiúsculo de minúsculo 

# Isso deixou fora do offset [10:20], slice não estava permintindo que retornasse os 
# nomes ao digitar na pesquisa. Estava retornando vazio.

# Agora fazendo a busca permitir encotrar por last_name.
# não da para acrescentar no filtro usandoa virgula(,) last_name. 
# Ao separar por vírgula a busca fica AND e isso faz com que o mesmo nome tenha que
# está no fist e last name.
# para isso precisa fazer um import.
# from django.db.models import Q

# O Q permite mudara consulta como ela é feita no Django.
# Com esse (Q) pode envolver um trecho da pesquisa e isso separa o first e last name
# pois ele permite usar um pipe | para fazer o OU na busca. Mas precisa retirar a vírgula
# .filter(
#     Q(first_name__icontains=search_value) |
#     Q(last_name__icontains=search_value)
# Usando um print depois do filtro para ver a cunsulta:
# veja o contact_fisrt OR contact_last na query.
"""
WHERE ("contact_contact"."show" AND ("contact_contact"."first_name" LIKE %Moura% ESCAPE 
'\' OR "contact_contact"."last_name" LIKE %Moura% ESCAPE '\')) ORDER BY 
"contact_contact"."id" DESC
"""
# Permitindo a busca filtrar além de fist e last name phone e email.
"""
.filter(show=True)\
    .filter(
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value)
"""
# A pesquisa tem suas limitações. Ele vai tentar da um match com fisrt_name, last,
# phone e email.
# Por exemplo a busca não permite nada muito complexo. Ele retorna vazio.
# a busca firará nesse nível Existem outras buscas para fazer com Django mas n será
# nesse projeto.
# O search ficou dessas forma:
"""
def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')

    context = {
        'contacts': contacts,
        'site_title': 'Search - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )
"""


# -------------------------------------------------------------------------


# 471 - Usando a request no template para pegar o valor de GET


# o formulário está apagando o valor e não está mantendo.
# existe várias maneiras de manter o valor.
# será usado o próprio valor q está sendo tratado - search_value.
# Pega esse valor, manda de volta no context e pegar o valor dentro do form
# basta colocar no base_templates/_header.html na class form coloque:
# value="{{ search_value }}"

# outra maneira é pegar o request pois temos acesso a ele em _header.html
# algumas funções pode chamar sem os parênteses e uma delas é o strip()
# por ela não receber nenhum argumento é fácil de chamar ela lá:
#  value="{{ request.GET.q.strip }}"

# evite jogar muita lógica p dentro do template. Mantenha a lógica na views


# Quando fizer a paginação - será mantido o valor da busca quando o usuário 
# estiver navegando entre as páginas.

# outra coisa, se não estiver exibindo contatos a tabela vazia é exibida.
# No templates/contact/index.html: 
# dentro do block e antes da divi faça um IF
# {% if contacts %} 
# o ELSE depois da div coloque:
"""
<div class="single-contact">
  <h1 class="single-contact-name">
    Nenhum contato encontrado
</h1>
"""


# -----------------------------------------------------------------------------


# 472 - Usando a classe Paginator para paginação no Django


# https://docs.djangoproject.com/en/4.2/topics/pagination/


# Paginator é uma classe do Djando pronta com vários recusros p criar a paginação
# basicamente está tudo pronto. A view, o template e a classe
# se quiser criar uma paginação mais robusta tem muitos valores nessa classe
"""
O Contact sera substituido pelo pag_objetic 
Na view foi substituido sendo assim, precisa substitui também no index.html
no IF e no FOR - troque contacts por page_obj
"""
# agora pegue toda a div do pagination e crei um partial 
# base_templates/global/partials/_pagination.html e cole a div do paginator

# uma alteração é: não exibir nada se não encontrar algo na agenda.
# coloque um if acima da div criada em _pagination.html

# No arquivo static do CSS já tem as classes criadas a partir do patination

# Agora precisa incluir esse arquivo no base.html da pasta global
#  Dentro da TAG <main>: {% include 'global/partials/_pagination.html' %}


# Acrescentando o mesmo trecho dentro da Views search e mudando o nome de
# contact para page_obj
"""
paginator = Paginator(contacts, 10)  
    page_number = request.GET.get("page")  # pega page do GET vai ta na url
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'search_value': search_value,
"""

# Ao fazer isso quando retorna uma pesquisa com duas páginas, ao ir para
# a segunda página ele perde a url anterior ficando somente a index.
# no arquivo _pagination.html acrescente em todos os links:
# &q={{ page_obj.GET.q.strip }}

# agora da para utilizar a paginação mesmo na busca.
# não perde a consulta nem o request get

# Paginação é meuo chato de fazer - por isso será mantida a mais simples


# ------------------------------------------------------------------------


# 473 - Usando um padrão comum para URLs de CRUD


# Organizando as urls para no futuro não ter problemas
# Vai seguir um padrão utilizado por outros devs
"""
EXEMPLO:
# Contact (CRUD)
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'), 
    path('contact/create', views.contact, name='contact'), 
    path('contact/<int:contact_id>/update', views.contact, name='contact'), 
    path('contact/<int:contact_id>/delete', views.contact, name='contact'), 
]"""
# Esse é o padrão comum de seguir em APIs, sites Django porque está mapeando a url
# Ao criar por exemplo as urls de user basta seguir o padrão. Tirar o contact e colocar user
# Assim fica fácil de entender o que as urls fazem só de olhar


# -----------------------------------------------------------------------------


# 474 - Criando a URL, view e template para criar um contato (CREATE)


# Ainda será criado o usuário. 
# Usuário, colocar user no contato, precisa está logado, etc. Só mais p frente.

# Crie um arquivo em templates/contact/create.html
# na maioria das vezes não precisa criar um templates para cada coisa.
"""
{% extends 'global/base.html' %}
{% block content %}
  <h1> CREATE CONTACT </h1>
{% endblock content %}
"""

# No packeage views crie um aquivo contact_forms.py para os formulários.
# crie o import no __init__: from . contact_forms import *
"""
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from contact.models import Contact

def create(request):
    context = {
    }
    return render(
        request,
        'contact/create.html',
        context
    )
"""
# na urls adicione o caminho:
# path('contact/create/', views.create, name='create'),


# -----------------------------------------------------------------------------


# 475 - HTML e CSS do formulário create.html


# No templates/create.html:
"""
{% extends 'global/base.html' %}
{% block content %}
<h1>CREATE CONTACT</h1>
<div class="form-wrapper"> -> p/ deixar o formulário menor
  <h2>Contact</h2>
  <form 
    action=""  -> será dinâmico e alterado depois
    method="POST"  -> método post: usado p coisas sensíveis user/password e tbm p enviar img
    enctype="multipart/form-data">  -> requerido em formulários quando envia arquivos
  >  
    <div class="form-content"> -> para agrupar coisas de mesma margem - uma separação visual
      <div class="form-group">  -> cria o label e o input
        <label for="id_first_name">LABEL</label>
        <input type="text" name="first_name" maxlength="255" id="id_first_name">
      </div>
    </div>
    <div class="form-content">
      <div class="form-group">  -> p criar o botão - do tipo submit p enviar o formulário
        <button class="btn" type="submit">Send</button>  
      </div>
    </div>
  </form>
</div>
{% endblock content %}
"""

# O django permite que a gente crie formulários e trabalhe com campo dinamicamente
# pois muita coisa desse html virá dinamicamente do form como o label, input, 
# os erros, o help text, a proteção do django CSRF - proteção de segurança do django


# -----------------------------------------------------------------------------


# 476 - csrf_token - proteção do Django contra ataques Cross Site Request Forgery


# de uma pesquisa por fora nisso.

# O django já vem por padrão em MIDDLEWARRE = [
#  'django.middleware.csrf.CsrfViewMiddleware', ]

# Vá em create.html no formulário, dentro da tag form e use a tag do csrf_token
# lembrando que é só para formulários do tipo post
# Essa tag gera um input do tipo hidden(escondido) com o código do Django que atualiza
# toda vez que acessa a página.
# Isso garante que os dados que chegaram na view realmente são os dados vindo do formulário
# Ao inpsecionar a página veja o que ele faz abaixo:
# <input type="hidden" name="csrfmiddlewaretoken" value="9DwThtxO7EqFYCMwTMcOezA7PBleQ2fatFPkNlJiR7faty09iR10WM7eqJl86vz1">
# outra atualização:
# <input type="hidden" name="csrfmiddlewaretoken" value="z1UlUzv66df4xsL0QmNlYRvJ9IeAkgQqT3dMqrHAQG4z2oZDfrCxG42QKQeuAJah">
# sempre diferente.


# -----------------------------------------------------------------------------


# 477 - Usando request.method e request.POST para saber quando o formulário é postado


# entendendo como o form funciona
# Nos inputs - o id e name precisam ser únicos na página
# O id é só para ter o identificador p o input - não é requerido
# O name é requerido - através do name é que pega a chave lá no request 

# Em create.html o form faz o método post p dentro da create.
# duplicando a div como exemplo tem o first_name e last_name
# acrescetando na views/contact_form.py - na função da p pegar o first e last name

# Quando acessa a página do formulário o método é o get
# Se digitar e enviar o método é o post
# Dentro da função da view existe duas possibilidades:
# GET para ler ou POST para salvar, cria e deletar algo.
# então é bom não deixar o método POST passar despercebido. Faça um IF
# if request.method == 'POST' ...
# Se for POST fará algo e se for GET vai passar e apenas renderizar

# É feito dessa mandeira quando trabalha com function base views
# Se trabalhar com class base views tem um método específico a ser chamado
# sem precisar fazer a lógica.


# -----------------------------------------------------------------------------


# 478 - Criando um formulário dinâmico com forms.ModelForm do Django P1


# Como temos o model contact - o formulário será criado baseado nele.
# Assim fica muito mais fácil de trabalhar.

# criando o formulário:
"""
# from django import forms
# Dentro de forms tem classes que pode usar para criar os formulários
# Para criar o formulário cria a class
# para criar o form do zero herdaria de (forms)
# Mas como já temos um formulário vamos herdar de (forms.ModelForm)
# É o formulário baseado no nosso modelo
# Na class: 
# precisa indicar qual é o model  que esse formulário é baseado e quais campos 
# desse model quer no formulário
# precisa criar uma meta class dentro para receber as configurações relacionada 
# com o form
# precisa indicar quais campos do model Contact quer que seja exibido no form
"""
# Como usar o form dentro do template:
# precisa passar o formulário no contexto

# da para criar o formulário usando tags do Django dentro do create.html
# mas vamos criar nosso próprio formulário veja:
"""
em create.html faça um FOR
  {% for field in form %}{% endfor %} -> recebe os campos de volta configurados no formulário
Dentro da tag for ficará a div para pegar os campos dinamicamente.
{% for field in form %}
  <div class="form-group">
    <label for="{{ field.id_for_label }}">{{ field.label }}</label>
field.id_for_label - pega o id do for no label.
field.label - pega o texto dos campos lá da view

# Agora o input: não precisa criar o input como estava antes.
Só de chamar {{ field }} ele cria o input dinamicamente. Veja os campos até então 3:
div class="form-group">
        <label for="id_first_name">First name</label>
          <input type="text" name="first_name" maxlength="50" required id="id_first_name">
        </div>
        <div class="form-group">
          <label for="id_last_name">Last name</label>
          <input type="text" name="last_name" maxlength="50" id="id_last_name">
        </div>
        <div class="form-group">
          <label for="id_phone">Phone</label>
          <input type="text" name="phone" maxlength="50" required id="id_phone">
        </div>
"""
# No contact_forms.py na função da views create.
# Quando enviar os dados, quer enviar eles para dentro do formulário precisa passar um atributo
# Quando sabe que o request.method é POST pode passar tranquilamente o request.POST que
# são os dados do formulário

# form que recebeu o post ele continua preenchido.
# Se entrar novamente na página o outro form limpa a página pois ele foi criado vazio.
# Quando o método é POST para no return. QUando o método é GET não entra no IF e renderiza
# a parte final do código com o form limpo
# Veja o código abaixo
"""
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }
        return render(
            request,
            'contact/create.html',
            context
        )
    context = {
        'form': ContactForm()
    } 
    return render(
            request,
            'contact/create.html',
            context
    ) """


# --------------------------------------------------------------------------------------


# 479 - Criando um formulário dinâmico com forms.ModelForm do Django P2


# Colocando no formulário em algum momento terá erros como nome inválido, senha,
# qualquer coisa que vc queria informar para o usuário para ele corrigir
# em create.html coloque um {{ field.errors }}
# Quando algum campo do formulário estiver com erro vai exibir uma msg

# Se existir erros de nonfilds - erros que não são dos campos:
# Primeiro checa com IF e depois pega os erros dentro da div:
"""
 <div class="form-content">
      {% for field in form %}
        <div class="form-group">
          <label for="{{ field.id_for_label }}">{{ field.label }}</label>
          {{ field }}
          {{ field.errors}}
        </div>
      {% endfor %}
  </div>"""


# ---------------------------------------------------------------------------------------


# 480 - Movendo o ContactForm para forms.py


# É bem comum no Django que utilize um arquivo no app contact chamado de forms.py
# Se ficar muito grande use a mesma tática da pasta views para separar
# Foi organizados os imports e retirado o formulário que era p teste que estava na view.

# -----------------------------------------------------------------------------


# 481 - Configurando os campos e widgets do formulário


# O django trabalha com widgets para campos de formulários

# https://docs.djangoproject.com/en/4.2/ref/forms/widgets/

# No models o campo first_name está assim:
# first_name = models.CharField(max_length=50)
# O widgets - CharField por padrão é um widgets de texto
# Por exemplo se quiser mudar o que está por padrão do Django:
# Se quiser configurar o passwold nesse mesmo lugar, vai em forms.py na classe meta
# do form e acrescente o widgets = {'first_name': forms.PasswordInput()}

# O widgets é o que está dentro do campo que vai ser renderizado no html
# Tem o campo de dentro do campo que vai para o html

# Dentro do widgets - tem um dicionário attrs = {} que é referente aos atributos
# do widgets. 
# É comum mudar em atributos:
# placeholder, classes p colocar no input
"""
class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
          'first_name', 'last_name', 'phone',
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                  'placeholder': 'Escreva aqui',
                }
            )    
        }"""
# Com esse placeholder se o campo estiver vazio ele mostra a msg 'Escreva aqui'

# outra forma de fazer isso seria acessar o __init__ da classe ContactForm
# Cria o init na classe mas precisa chamar o __init__ de quem está herdando
# Assim como no Python.
# Tendo acesso ao __init__ da class pode pegar o self.fields
# Isso retorna um dicionário que tem a chave como os campos
# Vamos fazer a mesma coisa feita com widgets no código acima usando o __init__:
"""
class ContactForm(forms.ModelForm):
    def __ini__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Veio do __init__',
        })"""

# Existe outra maneira mas que tem opções de modificar o campo inteiro.
# Essa seria a melhor maneira caso queria colocar algo diferente do que está no Models.py
"""
class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Outra maneira:',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para o usuário',  # precisa renderizar no create.html
    )"""
# No create.html adicione o help_text:
"""
% if field.help_text %}
  <p class="help-text"> {{ field.help_text }}</p>
{% endif %}
"""
# Esse método sobrescreve se por acaso estiver usando verbose_name no Models


# -------------------------------------------------------------------------------------


# 482 - Validando campos do formulário com clean, clean_field e ValidationError


"""
O usuário mandou algo que eu nãoquero enviar para a base de dados. 
Como avisar o usuário isso?
Existe várias maneiras - umas delas é usar o método clean
O método clean tem acesso a todos os campos do formulário.
Irá usar o método clean geralmente quando estiver validando um campo que depende 
de outro campo, quando estiver validando algo que não está relacionado com o campo
em si mas o formulário inteiro.
O clean é chamado antes de salvar na base de dados. Ele garante que se adicionar um 
erro ValidationError() ele n deixa salvar na base de dados. Ele apenas mostra os
erros no campo.

Mas tem outra maneira - é o clean com o nome do campo
Exemplo: validar o first_name:
Por está trabalhando no campo - valida um campo em específico
Se precisa apensa do valor de um campo. Use essa maneira.
# Usar o add_error é melhor posi ele pega tds os erros e exibe de uma vez.
# Mas se levantar uam excessão pode ser que ele não pegue tods e sim apenas do campo específico
def clean_first_name(self):
      first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                  'Não digite ABC nesse campo',
                  code='invalid'
                )
            )      
      return first_name"""
# se passou da validação quer dizer que está correto - return first_name: valor correto

# Agora quando um campo depende de outreo campo. Por exemplo o password.
# Depende do password e ca confirmação do password.
# Exemplo usando o primeiro e último nome: Assim a msg será exibida nos dois campos
"""
def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                    'Primeiro nome não pode ser igual ao segundo',
                    code='invalid'  
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()"""

# Nos dois métodos todos os dados vem do cleaned_data 


# ----------------------------------------------------------------------------------------


# 483 - Adicionando mais campos no formulário de contato


# Adicionando email, description e category por enquanto
# O email é validado automaticamente pelo Djanago 
# O description é uma text área
"""
class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category'
        )"""

# Validação OK. 
# ainda precisa usar o formulário p salvar na base de dados


# -------------------------------------------------------------------------


# 484 - Verificando form.is_valid, salvando com form.save e redirecionando a pag


# Na views/contact_forms.py def create que está usando aquele form...
# faremos alguams mudanças
# sempre que utilizar o form do Djando precisa fazer um if form...
# if form.is_valid():
#     contact = form.save()
#     contact.save()
# quando o tem um formulário Django se chama o método form.isvalid() quer
# dizer que não tem nenhum erro no formulário e pode salvar na base de dados
# forms.save() - salva os dados na base
""" 
if form.is_valid():
            contact = form.save(commit=False)
            contact.show = False
            form.save()"""
# commit = False: não salva ainda pois ainda será feito mudanças como colocar
# o contact.show = false

# outra observação é: limpar os dados quando o user enviar os dados para não correr
# o risco de que o user envie sem querer ou não várias vezes
# Mas como  ainda não te uma view para editar os dados do contato vamso só atualizar a pag
# O correto é:
# Ao criar o contato, manda ele p outra view onde vai ser editando os dados do contato

# no Django não tem um mmetodo que atualzia a página.
# O que pode ser feito é uma requisição para a mesma página
# Se o formulário for válido trave ele com um return para não exibir a mesma coisa
# com o return render(request)
# import o redirect
""" 
if form.is_valid():
    form.save()
    return redirect('contact:create')"""

# O user fica na mesma página mas limpa o formulário dele.
# A ideia é redirecionar para uma página que o user possa aditar o contato
# contact/id/update por exemplo. Será feito mais p frente.


# -------------------------------------------------------------------------


# 485 - Usando instance do ModelForm para atualizar dados de um contato


# No base_static/base_templates/partial/_header.html
# Coloque uma url no link:
# <a href="{% url 'contact:create' %}" class="menu-link">

# Agora como pegar a url do template mas dentro da view?
# <form 
#    action="{% url 'contact:create' %}

# faça o import:
# from django.urls import reverse
# com isso consegue passar dados para dentro dessa função reverse para que 
# retorne uma url do contato

# Quando o user for enviar o formulário essa ulr tem que ir dinamicamente de
# dentro da view
# Serão duas views:
# uma para criar e outra para atualizar o user

# Como serão duas views diferentes precisa passar p dentro do template uma 
# variável em create.html no form action
# <form action="{{ form_action }}"

# para saber o reverse do template create:
# Cria a variável e passa a url: form_action = reverse('contact:create')

# se o forumlário for válido form.is_valid() tem que redirecionar a página para outro local
# e passe o parâmetro dinâmico do update.
""" 
if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)"""

# Criando a url para direcionar: contac:update com o parâmetro dinamico <contact_id>
# path('contact/<int:contact_id>/update/', views.update, name='update'),

# coloque o form_action nos dois context 
"""
context = {
            'form': form,
            'form_action': form_action }
context = {
        'form': ContactForm(),
        'form_action': form_action, }"""

# A views contact_forms.py ficou assim:
""" 
from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.urls import reverse

def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        context = {
            'form': form,
            'form_action': form_action, 
            }
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk
            )
        return render(
            request,
            'contact/create.html',
            context)
    context = {
        'form': ContactForm(),
        'form_action': form_action, 
    } 
    return render(
            request,
            'contact/create.html',
            context)   """

# Criando a nova view update para atualizar contatos - serão bem parecidas.
# Criando em contac_forms.py - no mesmo arquivo

# tem que receber dinamicamente o contact_id
# Esse update vai atualizar um contato então precisa ter um contato.
# Feito as modificações...

# quando tudo tiver válido vai redirecionar para a view update

# Quando tem algum erro no formulário o action dinâmico continua sendo create

# Se o formulário é válido - a página tem que ser redirecionada para contact:update
# passando o contact_id=contact.pk
# AI cai na view update onde tenta buscar o contato p preencher o instance=contact
# do formulário.

# agora na página de criação do contato ao enviar o contato continua na
# página mas agora não envia contatos iguais e sim atualiza o mesmo contato
# mesmo que não faça nenhuma modificação e a url modica de create para update
# Criação: http://127.0.0.1:8000/contact/create/
# Update: http://127.0.0.1:8000/contact/1007/update/
 
# A diferenteça do create para o update:
# além de algumas lógicas é basicamente saber qual a instância instance=contact
# Precisa existir uma instãnca de um contato qualquer p atualziar
# E quando está criando não precisa da instância só precisa receber os dados do 
# formulário.
# Por isso é melhor criar duas views do que ficar fazendo IFs nas views.
# As duas views ficaram assim:
"""
from django.shortcuts import get_object_or_404, render, redirect
from contact.forms import ContactForm
from django.urls import reverse
from contact.models import Contact


def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        context = {
            'form': form,
            'form_action': form_action, 
        }
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context
        ) 
    context = {
        'form': ContactForm(),
        'form_action': form_action, 
    } 
    return render(
            request,
            'contact/create.html',
            context
    )   

def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        
        context = {
            'form': form,
            'form_action': form_action, 
        }
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context
        )
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action, 
    } 
    return render(
            request,
            'contact/create.html',
            context
    ) 
"""


# -----------------------------------------------------------------------------


# 486 - Criando a view, url e template para "delete" (apagar contatos)

# CSS adicionado no base_static/global/css/style.css
"""
.contact-links {
  margin-block: calc(var(--small-font-size) * 2);
  display: flex;
  align-items: center;
  gap: 0 var(--spacing);
}
.btn-link {
  font-size: var(--small-font-size);
  text-decoration: none;
  font-weight: bold;
  padding: 1rem;
  display: block;
  line-height: var(--small-font-size);
}
.btn-delete {
  background: tomato;
}
"""

# O botão delete ficará na página contado/id para que não seja fácil deletar o contato

# Em templates/contact/contact.html criará uma div
"""
<div class="contact-links">
      <a class="btn btn-link" href="{% url 'contact:update' contact.id %}">Update</a>

      <form action="{% url 'contact:delete' contact.id %}" method="POST">
        {% csrf_token %}

        {% if confirmation == 'no' %}
          <input type="hidden" name="confirmation" value="yes">
          <button class="btn btn-link btn-delete" type="submit">Confirma?</button>
        {% else %}
          <button class="btn btn-link btn-delete" type="submit">Delete</button>
        {% endif %}
      </form>
    </div>
"""

# todo link é uma requisição do tipo GET para o navegador.
# Quando faz uma requisição do tipo GET está informando que quer ler.

# O delete vai alterar algo na base de dados então ele tem que ser dentro de um form
# O delete vai ser um botão
# Sempre que for criar, editar e apagar algo na base de dados o método é o POST
# Todo formulário do tipo post no dJngo precisa do {% csrf_token %}
# Iniciando a criação da view delete:
"""
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    confirmation = request.POST.get('confirmation', 'no')  <-criando um input com name confirmation

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )
"""
# Se o confimation for no - muda o texto do botao e cria um input com confirmation yes


# -----------------------------------------------------------------------------


# 487 - Trabalhando com ImageField no template e nos forms


# O contato inteiro está sendo pssado para contact.htm, pode mostrar a imagem dele nessa pag
# Se existir imagem será exibida na página do contato. O if é para se não existir
# a imagem não quebre a página que não tenha imagem.
"""
{% if contact.picture %}
  <p>
    <img src="{{ contact.picture.url }}" alt="{{ contact.first_name }} {{ contact.last_name }}">
  </p>
{% endif %} """


# Na página de update precisa mexer no form
"""
 class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture') """

# O django acrescenta um link no p/ imagem no update
# A ideia é exibir a imagem e ter um botão para a pessoa enviar uma nova imagem

# No campo picture será mudado o widget
# Na contact/forms.py:
"""
class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )
"""
# No templates/contact/create.html: para exibir a imagem
# É preciso saber quando terá o campo chamado de picture e se tem uma url:
# Faça um IF dentro do FOR 
"""
{% if field.name == 'picture' and field.value.url %}
    <div class="form-group">
      <img src=" {{ field.value.url }}" alt="">
{% endif %} """

# Agora ao enviar a imagem nada acontece
# no contact/views/contactf_forms.py
# todo lugar que estiver recebendo POST coloque o segundo parâmetro request.FILES
# Mais precisamente na função create e update
"""
def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
...

def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES ,instance=contact)"""

# Está tudo OK. SE quiser trocar o arquivo basta escolher outro e enviar.

# Ao deletar o contato - se olhar no MEDIA o arquivo não será deletado
# Por padrão não deleta. Os arquivos ficam no servidor.
# Se quiser deletar a imagem tem que usar signaus


# -----------------------------------------------------------------------------


# 488 - Usando UserCreationForm para criar novos usuários no Django


# Trabalhando no owner 
# O owner é um usuário logado 
# Precisamos permitir o user seja criado para que logar e usar.

# Em contact/templates/forms.py - faça a importação:
# from django.contrib.auth.forms import UserCreationForm
# é um formulário que cria usuário - já está pronto.
# se não quiser nada complexo só o imorte e a criação da classe serve

# Para rederizar o form precisa de um template
# O form do template/contact/create.html é super dinâmico e funciona com
# qualquer form que colocar.
# Com isso vamos duplicar o arquivo create.html e tirar algumas cosias q não serão usadas.
# O template será register.html

# Crie a view para renderizar em:
# templates/views/user_forms.py
# O arquivo foi criado pois não estamos usando o contact e sim com user_forms
# não esqueça de importar tudo dele no __init__.py
"""
from django.shortcuts import render

def register(request):
    return render(
        request,
        'contact/register.html',
    )
"""

# Nas urls crie o user:




