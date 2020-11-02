# Model Relationship

- Many to One(1:N)

>  ForeignKey() <--  `외래키`



- Many to Many(M:N)

>  ManyToManyField()



- One to One(1:1)

>  OneToOneField()



## Many to One(1:N)

- 댓글기능 구현하기
- Article은 1개 / 댓글은 N개 => 1:N의 관계
- Article에 댓글을 참조할 경우 -> 여러개의 댓글을 참조하게 됨 ==> `X`
- 댓글테이블에 Article을 참조할 경우, 댓글하나당 1개씩 참조가능 ==> `O`
- 참조하는 데이터 == 댓글 (N) / 참조되는 데이터 == 게시글(1)
- 참조 무결성 원칙 -> 참조되는 데이터베이스(부모테이블)는 반드시 해당 테이블의 유일한 값이어야한다  => 일반적으로 ID를 사용(유일하니까)



### ForeignKey() 

>  django에서 Many to One(1:N)를 구현하기 위한 클래스

2개의 위치인자가 필요하다

1. 참조하는 모델
2. on_delete 옵션



1. django 프로젝트 활성화
2. accounts / articles ==> 두개의 app 이 존재
3. 댓글은 articles로 고고



1 (articles)의 모델은 건들지 않음

N(comment) 의 모델을 건들기

클래스 변수는 참조하는 테이블의 소문자 단수형으로 작성한다(약속이니까)

```python
# Article 클래스 하단


class Comment(models.Model):
    article= models.ForeignKey(Article, on_delete=) # 참조하는 클래스 이름,  
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

ondelete => foreignkey로 참조되는 객체가 삭제되었을 경우 어떻게 처리할 건가?

- `CASCADE` 가장일반적인 경우!! 부모 객체가 삭제됐을 때, 이를 참조하는 객체도 삭제
- Protect 참조가 되어있는 경우 오류 발생 -> 댓글이 있다면 게시글을 못지우게
- SET_NULL 부모객체가 삭제되면 모든 값을 NULL로 치환
- SET_DEFAULT : 모든 값이 DEFAULT로 -> default 값 설정해줘야함
- SET() : 특정함수 호출 -> 특정 함수를 정해줘야함
- DO_NOTHING : 아무것도 하지않음  / 데이터 베이스 필드에 대한 제한 조건을 설정해야함
- RESTRICT : protect와 비슷하나 특정한 경우 삭제할 수 있다

- 대댓글은 재귀적 외래키 -> 자기자신을 참조하게 됨





- shell_plus를 이용하여 확인해보자!

```sh
$ pip install ipython
```

> ipython 설치

```sh
$ python manage.py shell_plus
```

```python
In [1]: comment = Comment()
# comment클래스를 통해 인스턴스 생성하기
In [2]: comment.content = 'first comment'
# 댓글 내용 값을 넣어주기~!
In [3]: comment.content
Out[3]: 'first comment'
# 확인해보기
In [4]: comment.save()
# 저장하기 
# Error 가 발생 ==> 왜??
# 데이터베이스에 pk부분에 Null이 들어가게 된 것 -> 몇번째 글에 댓글을 작성하는지를 넣어주지 않음
In [5]: article = Article.objects.get(pk=1)
# 아까 작성했던 첫번째 글! 의 정보를 가져와보자
In [6]: article
Out[6]: <Article: 1번째 글>
# 글이 article에 저장됨
In [7]: comment
Out[7]: <Comment: first comment>
# comment에 저장된 Comment 작성내용
In [8]: comment.content
Out[8]: 'first comment'
# 현재 저장은 안된 상태
In [9]: comment.article = article
# comment의 article 클래스에 객체를 통채로 넣어주기 굳이 article.pk 안함
In [10]: comment.save()
# 저장 가능
In [11]: comment
Out[11]: <Comment: first comment>

In [12]: comment.pk
Out[12]: 1
# 1번째 댓글
In [13]: comment.article
Out[13]: <Article: 1번째 글>
# comment가 등록된 글
In [14]: comment.article.pk
Out[14]: 1

In [15]: comment.article_id
Out[15]: 1
# 1번 글에 작성
In [16]: comment.article.title
Out[16]: '1번째 글'
# 이와 같이 댓글을 통해 글의 정보를 확인할 수 있다.

# 두번째 댓글 달기!
In [17]: comment = Comment(content = 'second comment', article=article)

In [18]: comment
Out[18]: <Comment: second comment>

In [19]: comment.save()

In [20]: comment.pk
Out[20]: 2
    # 2번째 댓글임을 확인
```



- admin 페이지에 확인

admin.py / comment 등록하기

```python
from django.contrib import admin
from .models import Article, Comment # 명시적 상대경로 표현

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
```



- comment.article -> 댓글 입장에서 글로 접근이 가능하다
- 글의 입장에서 댓글을 확인하는 방법은?
- 1:N 의 경우에서 N이 1을 참조한다, 그렇기에 article 정보를 받아온다. 그렇기에 조회가 가능한데,,
- 글 입장에서는? ==> 역참조 가능하다
- 역참조시 가능한 명령어 있다 `comment_set`
- `comment.article` <- > `article.comment_set`



- shell_plus로 확인!

```python
In [1]: article = Article.objects.get(pk=1)

In [2]: article.pk
Out[2]: 1

In [3]: article.comment_set.all()
Out[3]: <QuerySet [<Comment: first comment>, <Comment: second comment>]>

In [4]: comments = article.comment_set.all()

In [5]: comments.first()
Out[5]: <Comment: first comment>

In [6]: comments.first().content
Out[6]: 'first comment'

In [7]: comments[0].content
Out[7]: 'first comment'
```





## related_name

- 부모 테이블에서 자식테이블 참조하는 것 

comment_set => 을 comment로 바꾼다면?

model에서 클래스에서 위치인자 뒤에 related_name='comments' 로 적어줌





## 페이지에 댓글 기능을 만들어보자



- urls.py 

```python
path('<int:pk>/comments/', views.comment_create, name='comment_create')
```



- modelform 활용을 위하여 forms.py에 들어간다



```python
from .models import Article, Comment # Comment 모델 추가해주기!


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        #fields = '__all__' # 다 넣으면, 페이지에 article 정보를 입력받게 됨
        exclude = ['article',] # article 칸은 제외하자!
```



- views.py

```python
from .forms import ArticleForm, CommentForm # 모델 폼 추가해주기
```





댓글은 get, post 나눌 필요 없음

detail 페이지에서 작성되고 있기 때문에! GET -> detail 페이지인 것.. POST 로직만 짜주기







댓글리스트 출력하기

detail _ view함수로 추가하기~!





## 댓글 수정하기

pass





### 댓글 삭제하기







## built and filter



django template tag and filters

![image-20200921160644712](C:\Users\qbw00\AppData\Roaming\Typora\typora-user-images\image-20200921160644712.png)





## get_object_or_404

- shortcut

Article.objects.get() -> 했을때 잘못된 정보가 넘어왔을 때 Not Found (404) 에러를 나와야하는데

.get으로 나오면 DoesnotExits(500) 에러가 나오게 됨