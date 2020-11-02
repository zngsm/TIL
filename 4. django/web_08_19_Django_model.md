# Django



## Model

> 데이터에 대한 단 하나의 정보소스, 저장된 데이터베이스의 구조를 의미
>
> 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함



-  django는 model을 통해 데이터에 접속하고 관리

- 일반적으로 각각 model은 하나의 `데이터 베이스` 테이블에 매핑된다





### 데이터베이스

> 체계화된 데이터의 모음
>
> 테이블, 열, 행, pk 4개의 구조

- `쿼리(Query)`를 날린다? => 질문을 날린다!

- 데이터를 조회하기 위한 명령어, 조건에 맞는 데이터를 추출하거나 조작하는 명령어

  

#### 스키마

> 데이터베이스의 구조와 제약조건에 관련한 전반적인 명세를 기술한 것
>
> 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조



#### 테이블

> 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합, SQL 데이터베이스에서는 관계라고도 불린다.

- `필드`, column, 속성 == 열  > integer, text, null 등 고유한 데이터 형식이 지정
- `레코드`, row, 튜플 == 행 > 테이블의 데이터가 저장된다



#### pk(Primary Key)

> 각 레코드의 고유값(==id), 반드시 설정해야한다.
>
> 데이터베이스 관리 및 관계 설정시 주요하게 활용된다



==> 이를 django에서 다루기 위해서 사용되는 것이 `MODEL`





## ORM

> `객체지향 프로그래밍 언어`를 사용하여, 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술

- 데이터베이스의 언어는 `SQL`

- Django의 언어는 `python`

  이 둘은 ORM 으로 연결될 수 있다

DB - SQL - ORM - python `object` - Model

-> python 만 사용할 수 있어도 orm이 sql도 조작해준다

`object` => python에서 OOP를 떠올리자

django에서 view 는 함수였다면, model 은 class이다!





## 실습

1. Model 내의 클래스를 생성하자.

- ```python
  .article(models.Model)
  ```

  - model 내의 클래스는 App 이름의 단수형으로 들어간다
  - 클래스 Model을 상속(실제 django 원본에 저장되어있는 클래스이다) 

- ```python
  title = models.CharField(max_length=10)
  ```

  - 길이의 제한이 있는 문자열을 넣을 때 사용한다
  - max_length는 필수인자 => 최대 길이를 설정. 기본 값은 `None` 이다
  - 글자수를 넘었는지, 데이터베이스와 `django`에서 유효성검사가 시헹된다
  - input type text로 출력된다
  - 이 경우 title은 CharField의 인스턴스

- ```python
  content = models.TextField()
  ```

  - 글자의 수가 많을 때 사용
  - 나머지는 CharField와 같다

- ```python
  create_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  ```

  - 최초생성일자 => `auto_now_add=True` (기본은 False 값이며 True의 경우 수정불가)
    - 최초 데이터 입력시에만 현재 날짜, 시간으로 갱신, 최초로 넣을때 들어가는 값
  - 최종 수정일자 => `auto_now=True`
    - Save할때마다 현재 날짜와 시간으로 갱신된다

- id? => django에서 직접 생성되기때문에 굳이 만들지 않는다





## migrations

> django가 model에 생긴 변화를 데이터에 반영하는 방법



- <b>makemigrations</b>
  - model 변경한 것에 기반한 새로운 마이그레이션을 만들 때 사용
  - 이는 곧 모델을 활성화하기 전에 db 설계도를 작성한다는 의미이다
  - 생성된 마이그레이션 파일은 데이터베이스 스키마를 위한 버전관리 시스템이라 볼 수 있다

- <b>migrate</b>
  - 작성된 마이그레이션을 DB에 반영한다 => 여기까지 완료되었을 경우에 테이블이 생성되는 것이다
  - db.sqlite3 파일을 확인할 수 있다
  - 모델에서의 변경 사항들과 db의 스키마가 동기화를 이루게 된다
- sqlmigrate
  - 마이그레이션에 대한 sql 구문을 확인할 수 있다
  - 해당 마이그레이션 파일이 sql 문으로 어떻게 해석되어서 동작할 지를 미리 확인
- showmigrations
  - 마이그레이션 파일들의 migrate 여부를 확인하기 위한 명령어
  - 프로젝트 전체의 마이그레이션과 각각의 상태를 확인할 수 있다
  - 지금 시점에 진행사항을 확인할 수 있으며, 반영되었을 경우 [x]로 앞에 체크되어있다
  - 모델의 문제가 발생하였을 때 확인할 수 있다



## 실습

```sh
$ python manage.py makemigrations
```

마이그레이션 생성 => migrations 폴더 내부를 보면 `0001_initial.py` 생성 확인

=> djang의 orm이 python을 sql로 해석되도록 만드는 것

model을 수정 후 위의 명령어를 다시 시행하면? => 0002가 등장한다

`makemigrations` 는 model 의 변경사항을 기록하는 역사이며, git 의 commit과 비슷한 역할을 수행한다

migrate는 가장 최신 migration을 반영한다



```sh
$ python manage.py migrate
```

터미널내의 뭔가 많이 업로드된 것을 확인할 수 있다. 해당 내용은 settings.py에서 확인했던 install 되어있던 django의 기본 app이 반영되었기 때문이며, 실제 작성한 내용은 1개임을 확인 할 수 있다 



-> 잘 반영되었는지 확인하고 싶다면?

vscode -> extension 중 sqlite install

기존 비활성화되어있던 dbsqlite3 -> 우클릭 open database 한 후 좌측하단에 sqlite explorer를 열어 작성한 appname - classname 에 해당되는 파일을 show table 하면 스키마 확인가능하다

데이터를 입력하지 않으면 no result found 라고 나온다



결론:

## Model의 중요 3단계

1. models.py : 변경사항(작성, 수정, 삭제,,) 발생
2. makemigrations : 마이그레이션(설계도) 만들기
3. migrate : DB에 적용



그렇다면, 반영된 데이터 베이스, 어떻게 쓸 수 있을까?





## DB API

> django가 기본적으로 orm에 제공한 것으로, db를 편하게 조작할 수 있도록 도와준다
>
> model을 만들면 django는 객체들을 `만들고(c) 읽고(r) 수정하고(u) 지울 수 있는(d)` database-abstract api를 자동으로 만든다 == database-abstract API 혹은 database-access API



### Making Queries

`Classname.Manager.QuerySet API`

- `Manager` = 데이터베이스 query 작업이 제공되는 인터페이스. 기본적은 django는 model class에 `objcet`라는 manager를 추가

=> 이하 object는 고정된다

- `Query Set` = 데이터베이스로부터 전달받은 객체목록으로, 내부 객체는 0개, 1개, 혹은 여러개일 수도 있다. 데이터베이스로부터 조회, 필터, 정렬 등 수행가능

=> 종류가 매우 다양하기 때문에 해당 공식문서 참고 필수!!



### Shell

```sh
$ pip install ipython django-extensions
```

python과 django의 업그레이드 shell을 다운받는다

shell 사용시 결과를 터미널 내에서 즉시 확인할 수 있다

```shell
$ python -i
>>> exit()
$ ipython
In [3]: exit()
```



#### django의 경우

1. pip install django-extensions
2. settings.py 에서 installed app에서 3rdparty의 위치에  'django_extensions' 를 추가
3. 기존 python manage.py shell  도 사용가능하나 전부 import 해줘야해서 불편
4. python manage.py shell_plus  을 사용한다

```shell
In [1]: Article.objects.all()
Out[1]: <QuerySet []> # 데이터를 따로 입력하지 않았기 때문에 비어있음
# QuerySeg 은 [] 이런 형태, 리스트와 같이 조작할 수 있다. 슬라이싱, 인덱스 등 가능
```



#### `C`reate 생성 `R`ead 읽기 `U`padate 갱신 `D`elete 삭제

> 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리기능



#### 1. create

1. 첫번째 방법

   1. article = Article() : 모델 클래스로부터 인스턴스 생성
   2. article 인스턴스로 클래스 변수에 접근해 해당 인스턴스 변수를 변경
   3. article.save() 메서드 호출 -> db 실제로 저장이 완료된다

   ```shell
   In [2]: article = Article() # 1. 인스턴스 만들어주기
   In [3]: article
   Out[3]: <Article: Article object (None)> # pk 값은 0 레코드에 작성된 값이 없어서
   In [4]: article.title = 'first'
   
   In [5]: article.content = 'django!' # 2. 인스턴스로 클래스 변수 접근해 인스턴스 변수 생성
   In [6]: article
   Out[6]: <Article: Article object (None)> # 엇.. 왜 none이지?!
   In [7]: article.save() # 3. 꼭 저장해야만 한다!!!
   In [8]: article
   Out[8]: <Article: Article object (1)> # pk 값이 생겼다
   # 드디어 dbsqlite3 에 글이 써진거다!
   ```

2. 두번째 방법

   1. 클래스로 인스턴스 생성 시 keyword 인자를 함께 작성
   2. `article = Article(title='second', content='django!'`)
   3.  article.save() 메서도 호출 -> db에 실제로 저장이 끝

   ```shell
   In [1]: article = Article(title='second', content='django!')
   
   In [2]: article
   Out[2]: <Article: Article object (None)>
   
   In [3]: article.save()
   
   In [4]: article
   Out[4]: <Article: Article object (2)>
   
   In [5]: article.pk # django는 id를 pk로 쓰는 것을 권장한다
   Out[5]: 2
   # article.id 도 동일하게 출력
   
   In [6]: article.title
   Out[6]: 'second'
   
   In [7]: article.content
   Out[7]: 'django!'
   ```

3. 세번째 방법

   1. create() 메서드를 활용하여 쿼리셋 객체를 생성하고 save까지 하는 로직을 한방에 가능
   2. `Article.objects.create(title='third', content='django!!')`

   ```shell
   In [8]: Article.objects.create(title='third', content='django!!')
   Out[8]: <Article: Article object (3)>
   # 세이브 안했는데 한방컷
   ```



> 점검해보자

```shell
In [9]: Article.objects.all()
Out[9]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>

# 객체가 3개 생성되었다!
```

위의 3번 다 create 수행되었음을 확인한다



※ 위와 같이 db는 object로 관리된다. 읽기가 불편하다면, shell 은 exit() 하고, models.py를 수정해보자.

선언했던 class 내부에 함수를 추가해준다

```python
def __str__(self):
       return self.title
```

-> 바뀐 내용을 makemigrations 해줘야할까?

답은 Nope. 로직 변경이 아닌, 보는 방식만을 변하는 거라 migration을 필요로 하지 않는다. 

다만 그걸 일일이 구분하긴 어렵기 때문에 model을 변경한다면 확인하는 것이 좋다

다시 확인

```shell
In [1]: Article.objects.all()
Out[1]: <QuerySet [<Article: first>, <Article: second>, <Article: third>]>
```

위의 선언한 함수대로 title로 나와서, 보기 훨씬 편안해졌다. 함수 내부는 내가 보기 편한 형태로 정의 가능. title이 가장 일반적이다





#### 2. Read

1. all()

   - 전체를 소환

   - `QierySet` return
   - 리스트는 아니지만, 리스트와 거의 비슷하게 동작 (조작할 수 있음)

```shell
In [1]: Article.objects.all()
Out[1]: <QuerySet [<Article: first>, <Article: second>, <Article: third>]>
```

2. get()

   - 특정한 객체 통해 query 하나만 소환

   - get(객체) -> 객체가 없으면, `DoesNotExist` 에러가 발생
   - 객체가 여러개일 경우는 `MultipleObjectReturned` 에러가 발생
   - 위와 같은 특징때문에 unique하거나 Not Null의 특징을 이용해 활용한다 => 주로 `pk`

```shell
In [2]: Article.objects.get(pk=1)
Out[2]: <Article: first>
# 변수를 지정해줄 수 있음
In [4]: aricle = Article.objects.get(pk=1)

In [5]: aricle
Out[5]: <Article: first>

In [7]: Article.objects.get(pk=100)
DoesNotExist: Article matching query does not exist.

In [9]: Article.objects.get(content='django!')
MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
```

3. filter()

   - 지정된 조회 매개변수와 일치하는 객체를 포함하는 QuerySet을 return
   - 값이 없을 경우도 빈 queryset을 소환. all과 같음

   - 같은 content를 가진 것을 전부 소환

```shell
In [10]: Article.objects.filter(content='django!')
Out[10]: <QuerySet [<Article: first>, <Article: second>]>
```





#### 3. Update

- 어떤 글을 수정할까? 선택해보자
  - get() 으로 시작한다
  - get으로 호출한 값을 받는 인스턴스를 생성
  - 해당 인스턴스의 값을 변경. 그리고 save까지

```shell
In [1] : article=Article.objects.get(pk=1)
In [2] : article='bye!'
In [3] : article.save()
```





#### 4. Delete

- 어떤 글을 지울까?
  - update와 동일하게 get을 통해 지우고자 하는 데이터를 지정한다
  - 삭제 즉시 반영. save 는 필요없다
  - 돌이킬 수 없으므로 신중히, 확인 후에 시행해야한다

```shell
In [1] : article=Article.objects.get(pk=1)
In [2] : article.delete()
```





## Admin

> 슈퍼유저를 만들어보자



터미널에서 아이디와 비번을 만든다

```sh
$ python manage.py createsuperuser
사용자 이름 (leave blank to use 'qbw00'): admin
이메일 주소:
Password:
Password (again):
비밀번호가 사용자 이름와 너무 유사합니다.
비밀번호가 너무 일상적인 단어입니다.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```



runserver 후 url/admin 을 넣은 후 로그인을 해보자



> model을 admin 페이지에 추가해주기

app 폴더 내의 admin.py에서

```python
from django.contrib import admin
from .models import Article # 명시적 상대 경로 표현법 `.` 중요함!!! 기억하라규,,,

# Register your models here.
admin.site.register(Article)
```



admin 페이지에서 model을 확인할 수 있다

object가 아닌 title인 이유는 위에서 -> `__str__` 해줬기 때문. 



주의사항: 반드시 db 구축 후 admin 계정을 생성해야한다.