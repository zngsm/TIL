# Model Relationship  + User

Article(1) : Comment(N)

Article(N) : User(1) < - NEW!

Comment(N) : User(1) <- NEW!



## 기본유저모델 -> 커스텀 유저모델로 대체하기

- 일부 프로젝트에서 django 내장 유저 모델이 제공하는 인증 요구사항이 적절하지 않는 경우가 있음
- `AUTH_USER_MODEL` : 유저 지정 모델을 참조해주는 설정값 -> 이를 변경하여 기본 유저 모델을 재정의 가능
- Django 에서는 기본 사용자모델보다 커스텀 유저모델을 설정하길 권장된다
- 커스텀 유저모델은 기본 유저모델과 동일하게 작동하지만, 필요한 경우 나중에 맞춤 설정할 수 있다
- 프로젝트의 `첫 migrate 실행 전` 완료해야함 



### AUTH_USER_MODEL

> User를 나타내는 데 사용하는 모델. 기본 값은 `auth.User` 



- 프로젝트 진행 중 값 변경 불가

- `Django custom Authentication` 검색하여 공식문서 확인 -> `Substituting a custom User model`

- ```
  AUTH_USER_MODEL = 'myapp.MyUser'
  ```



## AbstractBaseUser & AbstractUser

- AbstractBaseUser : paww_word와 last_login만 기본적으로 제공 -> 자유도는 높으나 필요한 필드 작성해야함
- AbstractUser : 관리자 권한과 함께 완전한 기능을 갖춘 유저모델을 구현하는 기본 클래스





## APP : accounts

- models.py

```python
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    pass
```

> 이와 같이 특별한 내용없이도 중간에 내용이 수정할 수 있기 때문에 migrate 이전에 User를 대체해줘야한다.(현재는 기능상 이전과 완전히 동일하다)



- settings.py

```python
AUTH_USER_MODEL = 'accounts.User'
```

> 가장 최하단에 넣어줘서, user를 대체해준다



- admin.py

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```



- 데이터베이스 초기화

1. migrations 지우기
2. DB지우기



UserCreationForm / UserChangeForm -> built-in form

기존 user와 연결되어있어서 다시 작성하거나 확장해야한다! 

- forms.py

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)
```



- views.py

```python
from .forms import CustomUserCreationForm

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```



--- User 대체작업 완료 ---





## APP : Articles 

- Articles / models.py

```python
from django.conf import settings
class Article(models.Model): # 상속
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

> user 참조하기

settings.py / AUTH_USER_MODEL  => models.py 유저모델을 사용할 때만 활용됨 / 그 외의 경우 get_user_model()

-> model 수정하였으니 다시 migrate?!

하지만 에러가 발생하였따. user의 foreignkey를 처음부터 설정하였다면 발생하지 않는데, 프로젝트 중간에 설정하여 문제가 발생됨!

-> default값을 설정하세요!

1. 자체적으로 터미널에서 default값 넣어주기

2. on_delete= models.CASCADE, `default=1`  로 추가해주기



- forms.py

```python
class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'content']
        # exclude = ['user'] 둘 중 하나 쓰기
```

> fields == all 상태면 user가 글 작성시 직접 user 선택을 해야함



- views.py

```python
@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) # 여기서 유저정보가 안들어옴
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```



- index.html

```html
{% for article in articles %}
    <p><b>작성자 {{ article.user }} </b></p>
{% endfor %}
```

django는 객체표현자체가 username으로 설정되어있음

사실.. article.user == article.user.username





## 댓글에 사용자 정보 입력하기



article.comment





`abstract = True` -> 데이터베이스에 반영되지 않지만 상속받은 애들한테 자기 속성을 부여해주는 것





모델링

- 현실세계를 최대한 유사하게 반영하기 위함
- 일상에 가까운 예시를 통해 db를 모델링하고 내부에서 일어나는 데이터의 흐름을 어떻게 제어할 수 있는지에 대해 고민

<hr>

우리 병원에 내원하는 환자와 의사 간의 예약 시스템을 구축.

의사 1명 - 환자 N 명 => 1:N 관계일까?

환자1명이 여러 의사에게 진료를 받을 경우? 

환자 1 : 의사들 N의 관계성립

Many to Many



stage 1. Doctor 모델과 Doctor를 참조하는 Patient 모델

```python
class Doctor(models.Model):
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    name = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```



```python
doctor1 = Doctor.objects.create(name='justin')
doctor2 = Doctor.objects.create(name='eric')
patient1 = Patient.objects.create(name='tony', doctor=doctor1)
# 위 상황에서 patient1이 추가로 doctor2의 진료를 받고 싶다면?
patient1 = Patient.objects.create(name='tony', doctor=doctor1, doctor2)
# ERROR!!
```

->  이를 해결하려면 중개모델을 활용할 수 있다



stage 2. 중개모델

```python
class Doctor(models.Model):
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
```



```python
doctor1 = Doctor.objects.create(name='justin')
patient1 = Patient.objects.create(name='tony')
reservation1 = Reservation.objects.create(doctor=doctor1, patient=patient1)
doctor1.reservation_set.all()
# 이와 같이 역참조를 통해 doctor시점, patient 시점에서 예약내용을 확인가능
```

> reservation을 활용하여 ManyToMany를 활용해보자



stage3. M T M

```python
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')
    # 위치 어디에나 상관없음! foreignkey는 위치가 중요했지만 manytomany는 다름
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
```



```python
In [1]: patient1 = Patient.objects.get(pk=1)

In [2]: patient1
Out[2]: <Patient: 1번 환자 tony>

In [3]: patient1.reservation_set.all()
Out[3]: <QuerySet [<Reservation: 1번 의사의 1번 환자>]>

In [4]: patient1.doctors.all()
Out[4]: <QuerySet [<Doctor: 1번 의사 justin>]>

In [5]: doctor2 = Doctor.objects.create(name='eric')

In [6]: Reservation.obejcts.create(doctor=doctor2, patient=patient1)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

In [6]: Reservation.obejcts.create(doctor=doctor2, patient=patient1)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
----> 1 Reservation.obejcts.create(doctor=doctor2, patient=patient1)

AttributeError: type object 'Reservation' has no attribute 'obejcts'

In [7]: Reservation.objects.create(doctor=doctor2, patient=patient1)
Out[7]: <Reservation: 2번 의사의 1번 환자>

In [8]: patient1.doctors.all()
Out[8]: <QuerySet [<Doctor: 1번 의사 justin>, <Doctor: 2번 의사 eric>]>
```

