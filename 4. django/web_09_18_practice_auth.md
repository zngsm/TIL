accounts/urls.py

```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
```



accounts/views.py

```python
from django.shorcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def signup(request):
    # user table 새로 뭔가 만드는 일
    # model, form 두가지를 이미 django에서 만들어 놓은 걸 쓸거다.
 
    # signup 로직 처리
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST) # data= 생략가능 첫번째 argument라
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    # signup page
    else:
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    # 로그인 시켜주기 => CREATE 로직
    # 사용자 - client 1000222411 값을 쿠키게 담아서 줬따.
    # 10000022411 - jang
    # 세션 기반 인증
    if request.method == 'POST':
        AuthenticationForm(request,request.POST)
        if form.is_valid():
            # 로그인
            # id, pw을 통해서 user가 있는 지 체크해야되고, == > form.get_user()
            # cliend - 쿠키에 세션 아이디도 적어줘야 하고,
            # server - 세션 아이디랑 사용자 정보 - 적어야하고
            auth_login(request, form.get_user()) # 위의 두가지를 실행해주는 장고으ㅣ 내장함수
            return redirect('accounts:index')
    # 로그인화면
    else:
        # 로그인 용 폼을 준다
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    # 로그아웃용 페이지가 필요한가? 놉
    # 로그아웃 - sessiong table에 해당 row를 삭제
    # 팔찌도 떼준다 -> 쿠키에서 세션 아이디를 삭제해준다
    auth_logout(request)
    return redirect('articles:index')
```





templates / accounts / signup.html

```html
{% extends 'base.html' %}
{% block content %}
<form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button>회원가입하기</button>
</form>
<a href="{% url 'accounts:index' %}">유저 목록으로 돌아가기</a>
{% endblock content %}
```

templates / accounts / login.html

```html
{% extends 'base.html' %}
{% block content %}
<form action="{% url 'accounts:login' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="로그인하기">
</form>
<a href="{% url 'accounts:index'%}">메인페이지</a>
{% endblock content %}
```



templates/accounts/forms.py < - form을 내장함수 그대로 쓰는게 아닌, 커스터마이징이 필요할때

```python
from django.contrib.auth.forms import UserChangeForm
from django.contirb.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'last_name', 'first_name')
```

