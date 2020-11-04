## Primeiros passos

Considerando que o python3 esteja instalado na máquina:

1) Inicialize um ambiente de virtualização.

``virtualenv -p python3 .``

2) Instale o Django.

``pip install django``

O comando acima irá instalar o mais recente. Para uma versão específica, use:

Ex.: ``pip install django==2.0.7``

Mais comandos:

``pip freeze`` - gera uma lista de dependências do projeto.

### Três formas diferentes de criar um virtual environment

1) ``virtualenv venv``

Funciona independente da versão do Python.

2) ``virtualenv venv2 -p python3``

Baseia-se na versão desejada.

3) ``virtualenv venv3 -p /usr/local/bin/python3``

O diretório é obtido usando o comando ``which python3``.

## Próximos passos

A partir da pasta "src".

### Comandos

``django-admin`` - nos permite fazer todo tipo de coisa com Django.

``django-admin startproject 'nomedoprojeto'`` . - cria um projeto Django

``python manage-py runserver`` - roda servidor de desenvolvimento

``python manage.py migrate`` - roda o banco de dados, sincronizando as configurações do 
projeto e de seus APPS.

### settings.py

É um arquivo importante, com muitas implicações para seu projeto.

import os -> importa o sistema operacional.

BASE_DIR -> é o caminho do diretório onde o arquivo manage.py está localizado.

Para testar, é possível usar ``print(BASE_DIR)`` no arquivo, para visualizar o caminho
ao rodar ``python manage.py runserver``.

SECRET_KEY -> todo projeto possui, é único e associado a cada projeto. Possivelmente pode levar
a vazamentos de segurança, então é uma boa idéia não torná-lo público!

DEBUG - Útil quando você está estudando ou desenvolvendo. Em produção, seu valor deve
ser definido como 'false'.

ALLOWED_HOSTS - 

INSTALLED_APPS - "aplicações" instaladas no projeto, são pequenas partes do projeto.
Já existem algumas definidos por padrão, ao criar um novo; É apropriado considerar os APPS como componentes.

MIDDLEWARE - Opera as suas requests e como as mesmas são tratadas, além de segurança e outros pontos.

ROOT_URLCONF - é uma forma do Django definir a rota de uma dada URL.

TEMPLATES - O Django renderiza templates em HTML, essa seção define onde serão armazenados e como serão
renderizados, como funcionam e etc.

WSGI_APPLICATION - Uma configuração usada pelo servidor. Normalmente não precisa ser alterada.

DATABASES - Mapeamento de base de dados, se define o banco usado como MySQL, POSTGRESQL ou outros.

AUTH_PASSWORD_VALIDATORS - Validação de senhas.

LANGUAGE_CODE, TIME_ZONE, USE_I18N, USE_L10N, USE_TZ - Configurações de internacionalização.

STATIC_URL - Onde os arquivos estáticos são armazenados, sejam imagens, CSS ou Javascript.

## Detalhamento de Apps

### auth e admin

``python manage.py createsuperuser`` -> cria um usuário que possui acesso ao admin.

user: sidnei
password: 1234a5678s

Agora, o usuário faz parte do banco de dados.

auth - foi a criação do usuário.
admin - foi a tela onde o usuário logou.

## Criando seu primeiro App Django

1) Vá até a raiz do projeto (onde está o arquivo manage.py).

Use pwd no terminal para ver seu diretório.

2) python manage.py startapp 'nomedoapp'

Cada app deve ser especializado para uma função. Por exemplo, um app de Produtos
deve lidar somente com ações relacionadas a produtos e nada relacionado a Blog.

### Armazenando dados em apps

Apps são excelentes em armazenar dados e mapeá-los para seu banco de dados.

"Eu quero armazenar um produto, e preciso que meu backend tenha memória de um produto 
o qual criei." Como?

Em ``models.py``:

class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()


Essa classe possuirá vários atributos, e preciso mapeá-los para o banco de dados.
- O método TextField() é uma opção.
- O produto em si precisa inheritar a classe Model, padrão do Django.
Isso permite o uso de muitas features importantes.

Assim, a classe irá mapear os dados para o banco de dados. Não esqueça de incluí-lo
na sua listagem de INSTALLED_APPS em "settings.py".

Para realizar a migração, rode ``python manage.py makemigrations`` e então
``python manage.py migrate``.

Obs.1: os comandos acima devem ser executados sempre que ocorrer alterações no arquivo
``models.py``.

Obs.2: Ao adicionar um novo item a ``models.py`` e rodar os comandos acima, irá retornar uma mensagem.
Para resolver, inclua um valor default na classe.

Agora, para acessar seu model de dentro do admin, inclua-o em ``admin.py``, localizado dentro da pasta do nome do componente (neste caso, products).

Em ``admin.py``, inclua:

from .models import Product
admin.site.register(Product)

Ao rodar ``python manage.py runserver``, a nova seção de Products estará disponível na tela inicial de admin,
e é possível adicionar um novo produto.

Obs.: comigo retornou um erro de:

OperationalError at /admin/products/product/add/
no such table: main.auth_user__old

Obs.2: Erro resolvido, usando:

``pip install Django --upgrade``

``python manage.py migrate``

``python manage.py makemigrations``

``python manage.py migrate``

No entanto, a tela exibe conteúdo incorreto para a localidade, com as seções de Groups e Users na mesma tela.

Rever o que ocorreu.

## Criando objetos de Products usando a Shell do Python

