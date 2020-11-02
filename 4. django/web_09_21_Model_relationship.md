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