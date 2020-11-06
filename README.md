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

``python manage.py runserver`` - roda servidor de desenvolvimento

``python manage.py migrate`` - roda o banco de dados, sincronizando as configurações do 
projeto e de seus APPS.

``python manage.py makemigrations`` - deve ser executado <b>sempre</b> que realizar alterações 
em models.py. Após o "migrate" deve ser usado.

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

## Model Fields

https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types

Alguns dos mais comuns (exemplificados em models.py) são:

TextField - é um campo grande de texto. O widget padrão para este campo é <b>Textarea</b>.

O parâmetro Null é usado para que o campo desejado seja aceito caso esteja vazio.

CharField - requer o uso do atributo max_length. No entanto, é similar a textField, só que envolve a contagem de caracteres.

DecimalField - usado para números decimais. Requer o uso dos atributos max_digits e decimal_places. (causou erros de tipo, int ou float, analisar)

EmailField - checa se o valor é um endereço de email válido; usa EmailValidator para a validação.

## Homepage - from default to custom

Rode ``python manage.py startapp pages`` e inclua o app `pages` em settings.py.

O arquivo <b>views.py</b> é o local responsável por gerenciar as várias páginas web do projeto, usando funções ou classes em Python.

A função abaixo é usada para criar uma página.

def home_view():
    return "<h1>Hello World</h1>" // é uma string simples

Para torná-la funcional, inclua ``from django.http import HttpResponse`` ao topo de views.py, então faça as alterações:

Obs.: args e kwargs são específicos ao Python. Pesquisar!

def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>") // é uma string simples

A função retorna um código HTML simples, dentro de uma HttpResponse.

No entanto, a "página" ainda não estará acessível. Primeiro, é preciso incluir a URL
correspondente à essa tela. Abra o settings.py e procure a linha com "ROOT_URLCONF".

O seu valor indica a localidade do arquivo "urls.py", onde as URLs são armazenadas.

A partir do mesmo, inclua o seguinte:

from pages import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
]

## URL Routing and Requests

- Padrões de URL e como trabalham em conjunto com a view.

É possível reparar que o primeiro argumento de path ('') é uma string vazia.

Isso quer dizer que a 'home' será a raiz do projeto, ou seja, seu index.

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
]

Através da mesma, podemos definr um novo caminho para a página a ser acessada.

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contacts_view, name='contact'),
    path('admin/', admin.site.urls),
]

Mais alterações foram realizadas em <b>views.py</b> e <b>urls.py</b>.

## Django templates

Processo que sempre ocorre: nós abrimos uma URL, o que faz uma requisição, e o servidor (ou Django) irá processar a URL sendo requisitada e retorna uma resposta, associando a URL com uma função apropriada ao
caso. Essa resposta será o HttpResponse retornado em cada view de <b>views.py</br>.

Para renderizar uma tela de conteúdo em HTML (ao invés de uma simples string), precisamos procurar um template:

def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})

Então, na pasta raiz do projeto (no caso, src), crie uma pasta "templates".

Abra o arquivo settings.py e vá até TEMPLATES. Em DIRS, copie o código dentro de
BASE_DIR no topo do arquivo. Ou seja:

'DIRS': [os.path.join(BASE_DIR, "templates")],

## Django templating engine basics/Inheritance in Django HTML Templates

O base.html é usado como "base" para as outras telas, as quais irão compartilhar o conteúdo em
comum entre elas.

Ou seja, evitando a repetição de componentes como header e footer, por exemplo.

Consulte os arquivos da pasta "templates" para maiores detalhes.

- Include template tag

Resumidamente, é uma forma de separar os componentes HTML.

Por exemplo, a navbar antes definida em 'base.html', agora é importada a partir de 'navbar.html'.

- template context

"adding new data coming from somewhere else"

Ou seja, recebendo dados do banco de dados e renderizando dentro do template.

O que é feito pelo Django: pega o template e o template context, une em um só arquivo, renderiza
e retorna HTML puro, o qual é visto pelo usuário.

Em views.py, podemos passar o contexto para cada template usando o {} (no Python, é chamado de 
dictionary). Exemplo:

def about_view(request, *args, **kwargs):
    # a key/value pair. the key is a string, but the value can be anything.
    my_context = {
        "my_text": "this is about me",
        "my_number": 123
    }

    return render(request, "about.html", my_context)

- for loop on a template

- conditions on a template

- template tags and filters

Usados até o momento foram extends, block, for, if.

## Renderizando dados provenientes do backend

Alterações realizadas no views.py de products.
