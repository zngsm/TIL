django last



many yo one relationaship

custon User model

change form

referencing user model

 -> get_user_model ==> 그외

Auth-User_model ==> models.py에서 사용



many to many

M:N 관계를 나타내기 위해 사용하는 필드

하나의 필수 위치인자가 필요하다

`django model field` => relationship field / manytomany

related_name => 역참조 이름

through => 중개 테이블을 직접 작성하려는 경우 지정(M:N 관계에 

장고가 중개모델을 만들어주지만, 추가데이터 필요경우 직접 만들어야함

symertrical => 재귀! (대댓글**)





좋아요

하나의 article에 여러 user가 좋아요 가능

한명의 user는 여러 article에 좋아요 누를 수 있다

1 : N

article -> user / article.user

user -> article / user.article_set // 유저가 작성한 게시글들

M : N

article -> users / article.users

user -> article  / user.article_set // 유저가 좋아요한 게시물 

둘이 겹쳐버림! 그러므로 relate_name 해줘야함

article -> 





font awesome >> 부트스트랩과 비슷하게 사용할 수 있다!



font Awesome Kits -> manage kit // new kit로 만들기

부트스트랩 cdn 아래에 작성하기



input 태그는 디자인이 어렵기 때문에 button 사용하기!

user가 게시글 좋아요 누른 유저리스트에 포함되어있는지 아닌지

if request.user in article.like_users.all():

단 전체 유저가 많아지면 탐색 시간이 많아진다!



전체 중 하나만 찾는 경우 user가 article을 좋아요 누른 전체 유저에 존재하는지로 탐색하는것이 권장

if article.like_users.filter(pk=request.user.pk).exists():

왜 pk를 사용해 조회하는데 get이 아니라 filter를?!

get은 빈 쿼리셋은 False / filter는 [] 으로 뜬다

좋아요를 아무도 누르지 않는 경우가 있기 때문에 filter로 써준다

`query set api` 찾기



팔로우 

유저와 유저의 관계!

![image-20200928125106840](C:\Users\qbw00\AppData\Roaming\Typora\typora-user-images\image-20200928125106840.png)