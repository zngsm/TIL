# 실습내용 정리



## 가상환경 설정

1. git bash here

```sh
$ python -m venv venv
```

2. vscode 실행

   1. python interpreter -> venv로 설정
   2. pip install django
   3. .gitignore 생성 / 공유x 파일 입력

   

## 프로젝트 시작

1. vs코드 가상환경 터미널 켜기

```sh
$ django-admin startproject crud .
$ python manage.py startapp articles
```

2. setting.py 에 app 추가해주기

```python
INSTALLED_APPS = [
    'articles', # 추가해주기
```

3. urls.py 에 app url 연결하기

```python
from django.urls import path, include

urlpatterns = [
    path('articles/', include('articles.urls')),
]
```



## Base template + Base static 생성하기

1. base template 만들기
   1. root 폴더에 templates 폴더 생성 후 base.html 생성
   2. 각 웹페이지의 기본적인 설정 후, 추가적으로 변경될 부분에 block 생성

```html
{% block content %}
<!-- 이안에 각 페이지별 내용이 들어간다 -->
{% endblock %}
```

2. bootstrap css / js 적용할 경우 root에 static 폴더 생성 후 base.css 생성하여 내용 작성하기

3. bootstarp download를 통해 cs / js 파일 다운 후 base.html에 적용해준다

```html
{% load static %}
<head>
  <link rel="stylesheet" href="{% static 'base.css' %}">
  <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
</head>
<body>
  <script src="{% static 'js/bootstrap.bundle.js' %}"></script>
</body>
```

4. settings.py 에 각 base 파일을 적용해준다

```python
TEMPLATES = [
    'DIRS': [BASE_DIR, 'templates'],
]
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```





## App의 MVT



### URLS.py

> app 폴더 내부에 urls.py 생성

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
]
```



### MODELS.py

> 저장될 데이터 테이블을 생성

```python
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



### VIEWS.py

> url을 받은 후 model에 데이터를 저장하고 응답할 내용

```python
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    render(request, 'articles/index.html', context)
```



### FORMS.py

> modelform 활용할 경우 생성

```python
from django import form
from .models import Article

class ArticleForm(forms.ModelForm):
    class meta:
        model = Article
        fields = '__all__'
```



### TEMPLATES

> 사용자에게 보여질 웹 페이지 구현

```html
{% extends 'base.html' %}
{% load static %}

{% block content %}
 <!-- 표현하고 싶은 html 작성 -->
{% endblock content %}
```



### BOOTSTRAP4

- 설치

```sh
$ pip install bootstrap4
```

- base.html

```html
{% load bootstrap4 %}

 {% bootstrap_css %}

 {% bootstrap_javascript jquery='full' %}
```

- settings.py

```python
INSTALLED_APPS = [
    'bootstrap4',
]
```

- forms.py

```python
class ArticleForm(forms.ModelForm):

    title = forms.CharField(
        label = '수정된 타이틀 라벨',
        widget = forms.TextInput(attrs={
            'class':'form-control'
        })
    )
```

- templates / **.html

```html
{% load bootstrap4 %}
{% bootstrap_form form %}
```



## CRUD

#### root 폴더

- urls.py

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 이미지에 url 부여한 것
```

#### app 폴더

- urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('update/<int:article_pk>/', views.update, name='update'),
    path('delete/<int:article_pk>/', views.delete, name='delete'),
]
```

- views.py

```python
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(data=request.POST, files=request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        'article' : article,
    }
    return render(request, 'articles/update.html', context)

@require_POST
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')
```

- models.py

```python
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default=100)
    image = ProcessedImageField(
        blank=True, 
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality':90},
        upload_to = '%Y/%m/%d/'
    )
    create_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add = True)
```

- template/articles/index

```html
{% extends 'base.html' %}
{% load static %}

{% block css %}
<link rel="stylesheet" href="{% static 'articles/index.css' %}">
{% endblock css %}

{% block content %}
<h1>메인페이지</h1>
<a href="{%url 'articles:create'%}">글쓰기</a>
<hr>
{% for article in articles %}
  <a href="{% url 'articles:detail' article.pk %}">
    <h1> {{article.title}}</h1>
  </a>
  <hr>
{% endfor %}
{% endblock content %}
```

- template/articles/create

```html
{% extends 'base.html' %}
{% load bootstrap4 %}

{% block content %}
<h1>글쓰기 페이지</h1>
<form action="{% url 'articles:create' %}" class="form" method="POST" enctype="multipart/form-data">
  {% csrf_token %}
  {% bootstrap_form form %}
  <button class="btn btn-primary">제출하기</button>
</form>
<a href="{%url 'articles:index'%}">메인페이지</a>
{% endblock content %}
```

- template/articles/detail

```html
{% extends 'base.html' %}
{% block content %}
<h1>상세페이지</h1>
<h2>{{article.title}}</h2>
<p>{{article.content}}</p>
{% if article.image %}
  <img src="{{ article.image.url }}" alt="{{ article.image }}">
{% endif %}
<ul>
  <li>{{article.create_at}}</li>
  <li>{{article.updated_at}}</li>
</ul>
<a href=" {% url 'articles:index' %}">메인페이지</a>
<a href="{% url 'articles:update' article.pk %}">수정하기</a>
<form action="{% url 'articles:delete' article.pk %}" method="POST">
  {% csrf_token %}
  <button>삭제하기</button>
</form>
{% endblock content %}
```

- template/articles/update

```html
{% extends 'base.html' %}

{% block content %}
<h1>수정 페이지</h1>
<form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
  {% csrf_token %}
  {{ form.as_p }}
  <button>제출하기</button>
</form>
<a href="{%url 'articles:index'%}">메인페이지</a>
{% endblock content %}
```



- image resizing module

```sh
$ pip installl pilkit
$ pip install django-imagekit
```

> settings.py

```python
INSTALLED_APPS = ['imagekit',]
```

> models.py