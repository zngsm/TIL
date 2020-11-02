[TOC]

# Django REST Framework



`10/05 10:00 ~ 11:30`

## API server

- API
  - 사용자 요청에 대해 서버가 데이터 응답해주는 것
  
  - 프로그래밍을 통해 json 응답하는 서버 만들기
  
    

## RESTFUL API

>  프로그래밍을 통해 요청에 RESTful한 방식으로 JSON을 응답하는 서버를 만들자



### REST

>  REpresentational State Transfer
>
> 자원과 주소의 지정방법

- 정보의 자원 URI 
- 행위 HTTP Method 
- 표현 Representations



#### URI 

> 통합 자원 식별자 (URI 하위로 `URL` : 파일 식별자 ==> 자원의 위치 /`URN`)
>
> 계층적 구조



![image-20201005102403539](C:\Users\qbw00\AppData\Roaming\Typora\typora-user-images\image-20201005102403539.png)

- Scheme / Protocol
- Host
- Port
- Path
- Query
- fragment : 브라우저에서 편의를 제공해주는 것



#### HTTP Method  

> 컨텐츠를 전송하기 위한 프로토콜

- 기본속성
  - `stateless` : 상태정보가 저장되지 않음
  - `Connectless` : 서버에 요청을 하고 응답을 한 이후에 연결은 끊어짐
- Method
  - GET : 지정 리소스의 표시를 요청하며, 오직 데이터를 받기만 함
  - POST : 클라이언트 데이터를 서버로 보냄
  - PUT / PATCH : 서버로 보낸 데이터를 저장 / 지정 리소스의 부분만을 수정
  - DELETE : 지정 리소스를 삭제



#### 표현 Representation

> 결론 : `json(JavaScript Object Notation)` 형태로 표기한다

- json : 언어 독립적인 text, 직렬화 및 역직렬화가 용이



#### 2가지 중심규칙

- URI는 `자원`을 표기하는 데 집중해야함 >> 행위는 url에 표기하지 않는다

- 자원에 대한 조작은 http method를 활용하자



## Django REST Framework(DRF)

- serialization(직렬화) : QuerySet이나 Model instance를 json이나 다른 데이터 타입으로 변경해주는 것

![image-20201005103826851](C:\Users\qbw00\AppData\Roaming\Typora\typora-user-images\image-20201005103826851.png)



## 실습 : django serializing



**더미데이터** 생성하기

- django seed : django 모델에 test data를 생성해준다
- 설치 후 installed_apps에 'django_seed', 추가
- $ python manage.py seed articles --number=20 (20개의 더미데이터 생성)



**serialize 하는 3가지 방법** https://www.django-rest-framework.org/api-guide/serializers/

1. 수기로 데이터 받아 json화 하기

```python
#views.py
from django.http.response import JsonResponse

def article_list_json_1(request):
    articles = Article.objects.all() # 전체 데이터 불러오기
    articles_json = [] # json 형태를 만들 리스트 생성
    for article in articles:
        articles_json.append({ # 일일이 항목을 지정해서 리스트에 추가해준다
            'id': article.id,
            'title': article.title,
            'content': article.content,
            'created_at': article.created_at,
            'updated_at': article.updated_at,
        })
    return JsonResponse(articles_json, safe=False) #safe=False에 주의할것 없으면 Error
```

> 서버를 켜보면 json 형태로 데이터가 저장된 것을 확인할 수 있다.
>
> 하지만 항목이 길어진다면, 수기입력 방식으론 불편하고 한계점이 분명하다



2. django 내장 serialize 활용하기

```python
from django.core import serializers
from django.http import HttpResponse

def article_list_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')
```

> 훨씬 간결해진 것을 확인할 수 있다. 하지만 내장 serialize로는 활용할 수 있는 범위가 제한적이다*



3. **model serialize**를 활용하자

```python
# app 폴더 내부에 serializers.py 를 생성한다
# serializers.py

from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer): # 모델폼 활용때와 유사하다
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at', 'updated_at',]
        
# views.py
from articles.serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET']) # 이건 required_POST와 달리, 작성해주지 않으면 실행조차 되지 않는다
def article_list_json_3(request):
    article = Article.objects.get(pk=1)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
```

> json화 되었고, 화면 역시 이전에 글자의 나열에 불과했던 화면에서 깔끔히 정리된 모습 확인가능
>
> 우린 앞으로 이것을 활용할 것이다.



`10/05 12:30~14:00`

**정리** 우리는 지금 무엇을 배우고 있는가? 뭘 배워왔는가?



`서버`란? html 웹 페이지를 보여준다

서버 안에는 모델(데이터베이스정보 < 게시글, 유저, 댓글 등), css 등 다양한 내용이 포함



우리가 어떠한 서비스를 만든다면 --> ???

1. `웹페이지` -> 우리가 배운 내용
2. 모바일 웹
3. 모바일 앱 IOS
4. 모바일 앱 Android
5. 기타 등등



이걸 일일이 전부 혼자 만든다고?!  --> `NOPE`

이제 웹 페이지를 만드는 것이 아닌, 만들기 위한 정보를 넘겨준다

정보의 format == `json` 



웹 페이지를 만드는 front-end 개발자

정보를 만들어서 넘겨주는 back-end 개발자 `new!`

모바일 어플리케이션을 만드는 app 개발자 ... .etc



`10/05 14:00~16:00`

DRF를 활용해 어떻게 CRUD를 구성할 수 있는가?!



- serializers.py

```python
from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Article
        fields = ('id', 'title',)
```



- python manage.py shell_plus



```python

```



- 



django status Code







REST API > url, method 정의하는 규칙

rest = url과 method를 정의하는 방식 중 하나

restful-

모든 게시글을 보여주는 서버 기능

/articles/show/ GET

/articles/show/ POST

method(행위), url(자원)

/articles/ GET < rest 규칙에 맞춘 url

