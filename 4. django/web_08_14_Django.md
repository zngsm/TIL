[TOC]

# django1_08_14

> python web framework
>
> 웹 개발과정에서 겪는 어려움을 줄여주기 위한



- 웹 프로토콜
  - 요청을 보내면 서버에서 응답. 장고는 서버를 만드는 것

- 일반적으로 `MVC` 패턴 (model view controller)

- django의 소프트웨어 디자인 패턴은 `MTV `방식 (model Template View)
  - `model` 데이터관리` Template` 인터페이스(화면) `View` 중간관리, 컨트롤러
  - 요청이 들어오면 템플릿에서 `데이터`를 가져와 `뷰` 함수를 통해 실행하여 사용자에게 `보여주는` 시스템



![image-20200817214809205](C:\Users\qbw00\AppData\Roaming\Typora\typora-user-images\image-20200817214809205.png)

1. HTTP Request 서버에 요청보내기
2. 요청을 URLS에 보낸다
3. **해당 요청을 View에서 실행한다**
4. Template에서 해당 페이지를 가져와서
5. Response 한다



## django 시작 



### vs code

extension - django 설치 후 (젤 위의 것 0.2.0) usage 내용과 아래 emmet 까지 복사한다

ctrl + shift + p => preference: Open Workspace Settings(Json) 에서 하단에 붙여넣는다.

터미널 후 장고설치 하고, 설치 list 를 확인한다

```sh
$ pip install django
$ pip list
```





### django 프로젝트 시행하기

- ##### 터미널에서 project 파일 생성하기

```sh
$ django-admin startproject first_project
```

- 주의사항 : 프로젝트 이름에 `-` , python, django의 예약어, 모듈 등 기본 이름 사용 불가

- first_project 라는 파일이 생성되었고 하위 폴더 안에 여러 파일들이 생성된다 

  우리가 사용할 것은 `urls.py` 와 `settings.py`

  - `__init__.py` : 빈파일, 작성할 일 X python에게 이 디렉토리를 하나의 패키지로 다루도록 지시
  - `asgi.py` : 비동기 웹서버와 연결, 소통을 도움. 배포시 사용됨
  - `settings.py` : 웹사이트의 모든 설정. app 등록~ static files, database 세부설정 등
  - `urls.py` : url 작성 - views.py 와 연결
  - `wsgi.py` : django가 웹서버와 연결, 소통하는 것을 도움. 배포시 사용.



### django 서버실행

```sh
$ python manage.py runserver
>> http://1276.0.0.1:8000/ 나의 로컬주소
>> ctrl+c = 서버 종료
```

> 처음에는 로켓페이지 확인가능하다



### django app 생성

> 실제 어떠한 역할 > app에서!
>
> 하나의 프로젝트는 이러한 어플리케이션의 집합 / 요청을 받고, 처리하여 페이지를 보여주는 것은 어플리케이션에서 발생한다
>
> 역할/기능별로 app을 쪼갤 수 있다

```sh
$ python manage.py startapp articles # 앱의 이름은 복수형이 권장된다
```

- 위에서와 동일하게, 많은 폴더가 생성됨
  - init 위에서와 마찬가지로 패키시 실행. articles에 접근할 수 있도록 만들어줌
  - admin 관리자 전용 기능
  - apps 앱에 대한 정보. 작성안할 예정
  - `models` 나중에 배움
  - tests 테스트 코드 작성
  - `views` 제일 중요함



- ##### app을 pjt에 등록

  - settings.py

```python
Installed_APPS = [
	# 1. local apps
	'articles(내가 만든 앱)',
	# 2. 3rd party apps
	# 3. django apps
	기본 설치되는 필수앱,
]
# 리스트의 마지막 요소에도 , 가 온다
```



- 언어 설정하기
  - settings.py

```python
LANGUAGE_CODE	= 'ko-kr' # 로 입력하면 한국어가 됨
```



## urls -> views -> template 순으로 작성하여 출력까지



### urls 작성하기

```python
from articles import views
# views 안에 함수 작성 후 들어올 것
urlpatterns = [
    path('index/' views.index(views.py에서 실행될 함수))
]
```



### views 작성하기

```python
def index(request): # 무조건 request를 첫번째 인자로 받아야한다
    return render(request, templatename-경로없어도 장고에 기본으로 설정되어있음) # render에서도 첫번째 필수인자 request
```

- django style import guide : Views에서 함수 작성을 위해 import 를 사용할 경우, 작성 순서

  1. standard library

  2. 3rd party library

  3. Django

  4. local django



### template 만들고 작성하기

- app 내에 폴더생성 -> `templates` 여야만 함
- 안에 html 파일 생성한다

```html
<!-- view가 리턴할 경우 보여줄 화면 html로 작성한다 -->
```



### 실습 : 랜덤활용하여, 저녁메뉴 추천 페이지 제작

> 위의 과정을 응용하여 랜덤으로 저녁메뉴 추천하기

```python
# urls.py
from articles import views
URLpatterns = [
    path('dinner/' views.dinner)
]

# views.py
import random

def dinner(request):
    menus = ['한식', '양식', '분식', '일식']
    pick = random.choice(menus)
    return render(request, 'dinner.html', {'key(pick)' : value(pick)})
# 함수의 리턴값은, 요청에 따라 dinner.html 파일을 불러오며, 해당 함수에서 content(현재 pick) 값을 불러온다. pick의 경우 딕셔너리로 작성해야만 한다
# 여기서 key-pick 이 templates에서 사용가능한 변수명 -> value 는 위 함수에서 해당 key값이 의미하는 변수명
```

```html
<!-- templates/dinner.html -->
<body>
    <h1>
        오늘 저녁은 {{ pick }} 입니다!
    </h1>
</body>
```



### variable routing

> 주소 자체를 변수처럼 사용해서 동적 주소 만들기



```python
# urls.py
urlpatterns = {
    path('hello/<str:name>/', views.hello),
}

# views.py
def hello(request, name):
    context = {
        'name':name,
    }
   	return render(request, 'hello.html', context)

# hello.html
<h1> 안녕하세요 {{name}}님</h1>
```

> 기본값이 str이므로 생략 가능 이외 int형으로도 사용가능하다





## Form을 활용한 throw & catch



### Form

> 웹에서 사용자 정보가 입력되는 여러 방식을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당하는 html 태그
>
> 한 페이지 --> 다른 페이지로 데이터 전달을 위해 사용된다
>
> `action` -> 입력데이터가 전송될 url / `method` -> 입력 데이터의 전달 방식(`get` or `post`)



- GET => 정보 조회시 사용 / 상태 변경 x 



### throw & catch

- throw

  ```python
  # first_project/urls.py
  
  path('throw/', views.throw),
  ```

  ```python
  # articles/views.py 
  
  def throw(request):
      return render(request, 'throw.html')
  ```

  ```html
  <!-- articles/templates/throw.html -->
  
  <form action="/catch/" method="GET">
    <label for="message">Throw</label>
    <input type="text" id="message" name="message">
    <input type="submit">
  </form>
  ```

- catch

  ```python
  # first_project/urls.py
  
  path('catch/', views.catch),
  ```

  ```python
  # articles/views.py
  
  def catch(request):
      message = request.GET.get('message')
      context = {
          'message': message,
      }
      return render(request, 'catch.html', context)
  ```

  ```django
  <!-- articles/templates/catch.html -->
  
  <h1>너가 던져서 내가 받은건 {{ message }}야!</h1>
  <a href="/throw/">뒤로</a>
  ```



- request
  - 요청 간의 모든 정보를 담고있다





## URL



### url분리

> app폴더에 urls.py 를 각각 작성함으로써 코드 유지보수를 편리하게 함



- 프로젝트 urls.py

```python
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
```

> `include`를 import하여 다른 url을 참조할 수 있도록 도와준다