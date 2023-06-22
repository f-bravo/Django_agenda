import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

# não é um scrip para ter no servidor de produção - gera muito transtorno

# Pegando o caminho até a raiz do projeto - o import será p trás
# terá que importar de settings, project.
# Está pegando a raiz para "enganar" o Python dizendo que a raiz tbm faz parte do pjt
DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

# Adicionando um caminho acima do DJANGO_BASE_DIR p importar coisas acima
# inclundo o caminho da raiz no sys.path - agora o Python busca nas pastas p/ trás
sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False  # para n ter que fazer configurações de timezone
"""
Sempre que for utilizar o Djando não sendo por manage.py, precisa configurar o
'DJANGO_SETTINGS_MODULE' falando onde está ele. O manage.py já tem o que precisa.
"""
# iniciando o Django - configura ele
django.setup()

if __name__ == '__main__':
# o faker geralmente é ultilziado para testes. Mas será usado para popular o bd 
    import faker

# As importações ficaram aqui para que n seja reordenada e n cause erros
    from contact.models import Category, Contact

# deleta tudo que foi criado anteriormente para testar - cuidado
    Contact.objects.all().delete()
    Category.objects.all().delete()

# configurando o faker forçar que seja nomes em português br
    fake = faker.Faker('pt_BR')
    categories = ['Amigos', 'Família', 'Conhecidos']

# gerando categorias e salvando no FOR
    django_categories = [Category(name=name) for name in categories]

    for category in django_categories:
        category.save()

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )
# Tudo será salvo em momória para depois serem criados todos de uma vez com bulk_create
# ao invés de ter 1000 querys, terá só uma na base de dados
    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)


