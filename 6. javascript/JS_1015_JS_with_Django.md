## 기존 로직

- 브라우저에 요청을 보내면 html 문서로 응답해보여준다
- html 문서를 통해 navbar, article list 등 확인가능



- 기존 로직에서 like를 누를경우 -> `302`found(정해진 페이지로 redirect)를 확인할 수 있다.
- 좋아요 설계 당시 -> like를 누르면 articles로 redirect 하게끔 설계되어있다.



- 좋아요 누를 경우 -> 기존 페이지와 동일하나 하트의 색깔과 좋아요 숫자가 바뀐다
- 고작 이거 때문에 페이지 요청을 보내 다시 redirect 하는 것은 너무나도 데이터 낭비가 아닐까?
- Js를 활용해 페이지내에서 정해진 하트와 숫자만 변동되며 페이지가 새로고침되지 않도록 해보자



- 로직 시나리오

1. like 버튼을 누르면

2. js가 요청을 한다

3. 요청을 받는 것은 django의 like부서이다

4. like 부서는 좋아요를 처리(db에다가 그렇게 쓴다) 응답으로 

   지금 요청을 한 애가 좋아하는 지 여부, 이 글을 좋아하는 사람수

   두가지 정보를 응답으로 준다

5. js는 응답을 받아서, 

6. 좋아요 버튼 색깔과, 사람 수 숫자를 바꾼다



- 기존

```html
<form action="{% url 'articles:like' article.pk %}" method="POST" class="d-inline">
      {% csrf_token %}
      {% if user in article.like_users.all %}
        <button class="btn btn-link">
          <i class="fas fa-heart fa-lg" style="color:crimson;"></i>
        </button>
      {% else %}
        <button class="btn btn-link">
          <i class="fas fa-heart fa-lg" style="color:black;"></i>
        </button>
      {% endif %}
    </form>
```

> button이 submit 되면 -> form이 action에 담긴 url로 post 요청을 보낸다 < 브라우저에서 관리



- 시나리오에 따라 수정해보자

0. 페이지 reload를 없애기 위해 form 태그에 action과 method를 주지 않는다. 이는 script내에서 처리될 것이다.

```html
<form action="{% url 'articles:like' article.pk %}" method="POST" class="d-inline"> <!-- 삭제 -->
<form class="d-inline">
```



1. form 을 받아오기

```js
const forms = document.querySelectorAll('.like-form')
```

> forms를 selectorAll 로 받아오는 이유 > 좋아요 누르는 form 객체를 배열 형태로 불러와야하기 때문에 클래스 지정하고 All로



2. 각 form에 forEach 이용하여 함수적용하기

```js
forms.forEach(form => {
      form.addEventListener('submit', (event) => {
        event.preventDefault()
        const articleId = form.dataset.articleId
        axios.post(`/articles/${articleId}/like/`, {}, { headers: {'X-CSRFToken': csrftoken} })
        .then( (response) => {
          const likeBtn = document.querySelector(`#like-btn-${articleId}`)
          const likeCount = document.querySelector(`#like-count-${articleId}`)
          if (response.data.liked) {
            likeBtn.style.color = 'crimson'
          } else {
            likeBtn.style.color = 'black'
          }"
          likeCount.innerText = response.data.count
        }) 
      })
    })
```



```js
forms.forEach(form => {
form.addEventListener('submit', (event) => {
event.preventDefault() }) })
```

> form 이 submin제출되는 이벤트가 발생할때마다 이하 함수를 실행한다
>
> 단 이하 코드가 실행되기전부터 submit이 발생해버려 url이 get요청을 받고 새로고침된다
>
> 이를 방지하기 위해서 일시정지 시켜주는 preventDefault를 넣어준다



해당 form은 각각 article마다 발생하는 것이기 때문에 articleId를 받아와야한다

하지만 html 내 form 태그에 article 정보를 받아오고 있지 않기 때문에 `data`를 활용하여 정보를 받아오자

```html
<form class="d-inline like-form" data-article-id="{{article.pk}}">
```

> `data-`article-id= 이 양식은 규칙이다.
>
> script내에서는 `-` 를 생략할 수 있으며, 대신 - 다음 문자는 대문자로 표기한다

```js
const articleId = form.dataset.articleId
```

> 이와 같이 script에서 받아올 수 있다.



Axios 활용하기

```js
axios.post(url, data, config)
```

> axios는 이와 같은 형태로 넣어준다. method가 POST였기 때문에 post로 넣어준다



```js
axios.post(`/articles/${articleId}/like/`, {}, {}).then( (response) => {
    
})
```

> 이와 같이 접근하게되면, 정보는 맞으나, 403 에러가 발생한다 >> 권한이 없기 때문에
>
> csrf token 정보를 같이 넣어줘야한다



csrf token 은 새로고침 할때마다 정보가 바뀌지만, 해당 페이지내에서는 동일한 value를 갖고 있다.

forEach에서 각각 받을 필요없이, 전역변수로 선언하여 사용가능하다

확인결과 csrktoken은 input 에 들어가 hidden 되어있었음 value는 새로고침해도 변동이 있지만 name은 고유하다. input 태그내의 name을 활용하여 csrktoken을 가져온다



```js
const csrfTokenInput = document.querySelector('input[name="csrfmiddlewaretoken"]')
```

> 위의 csrkToken에서 value가 필요하다

```js
const csrftoken = csrfTokenInput.value
```



이를 어디에 활용해줘야하나?

공식문서 확인 결과 headers에 담아 `{headers: {'X-CSRFToken': csrftoken}}` 와 같이 담아준다

이 정보는 axios의 config에 해당하는 인자이다.



```js
axios.post(`/articles/${articleId}/like/`, {}, {headers: {'X-CSRFToken': csrftoken}}).then( (response) => {
    
})
```

> 위치인자가 중요하기때문에 data가 없다하더라도 빈칸으로 남겨줘야한다



주요로직은 완료. 이제 views를 수정하여 redirect 페이지가 아니라, 좋아요와 좋아요 수를 변수로서 보내주도록 한다

```python
@require_POST
def like(request, article_pk):
    context = {
        'error':'unauthorized'
    }
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        user = request.user
        

        if article.like_users.filter(pk=user.pk).exists():
        # if user in article.like_users.all():
            article.like_users.remove(user)
            liked = False # 좋아요 취소하는 경우
        else:
            article.like_users.add(user)
            liked = True # 좋아하는경우
        # 이 유저가 좋아하는지 안 좋아하는지
        context = {
            'liked' : liked,
            'count' : article.like_users.count()
        }
        # 이제 django.http 에서 jsonresponse를 import 해오기
    return JsonResponse(context)
```

> 좋아요 일 경우, True, 아닐 경우 False를 표현해주는 liked 변수와, 좋아요 총 수를 표현하는 count를 담아서 Json으로 값을 반환해준다.



console로 확인하면, 해당 변수를 읽을 수 있고 이를 통해 내부에선 좋아요와 좋아요 취소가 반응함을 알 수 있다. 다만 하트 색과 숫자명은 html로 표기되어있기 때문에 받아오지 못하는 중.

이를 조건문을 통해 설정해준다.

html에서 해당 하트와 숫자에 id를 넣어줘서 script에서 선언해준다.

```html
<button class="btn btn-link">
          <i id="like-btn-{{article.pk}}" class="fas fa-heart fa-lg" style="color:crimson;"></i>
        </button>
<span id="like-count-{{ article.pk }}">{{ article.like_users.all|length }}</span>
```



```js
const likeBtn = document.querySelector('#like-btn-${articleId}')
const likeCount = document.querySelector('#like-count-${articleId}')

if (response.data.liked) // 좋아요=True {
    likeBtn.style.color = 'crimson'
} else {
    likeBtn.style.color = 'black'
}

likeCount.innerText = response.data.count
```

> 좋아요 버튼과, 좋아요 숫자의 id를 활용해 변수로 선언해준다
>
> 조건문을 활용하여, 좋아요 버튼의 색을 지정해주고, innerText를 통해 숫자도 넣어줄 수 있다.



- user 정보는 어떻게 담기는건가?

쿠키에 세션아이디에 저장되어있음! header에 쿠키 정보가 같이 넘어간다







워크샵 과정



1. 팔로우를 요청하는 form을 받아서 선언해주기
2. form이 submit되는 event 발생시 함수시작~
3. 일시정지
4. axios를 통해 url에 post 요청을 보내기, csrf token 담아서 << 그 전에 userId를 정의해주긴
5. 데이터를 무사히 전송하였다면, 데이터 확인해보기 >
6. views를 통해 follow들의 변동정보와 follow수를 담아주는 변수를 전송해주기
7. 해당 변수들을 활용하여, html 에 있는 태그들에 클래스나 id를 붙여줘 선언하고
8. 작동시마다 색과 텍스트가 변경되도록 하기





1. follow버튼 - form에 클래스명 "follow-form"

> script로 넣었고, form은 하나밖에 없기때문에, 클래스보다는 id로 넣는것이 더 편안





![image-20201015164918420](C:\Users\qbw00\AppData\Roaming\Typora\typora-user-images\image-20201015164918420.png)

![image-20201015171837186](C:\Users\qbw00\AppData\Roaming\Typora\typora-user-images\image-20201015171837186.png)

