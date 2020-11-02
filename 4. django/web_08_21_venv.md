### 가상환경

> 시스템 파이썬에 설치된 모든 라이브러리와 격리되어있는 파이썬 환경으로, 고유한 파이썬 환경을 가지며 독립적으로 설치된 패키지 집합을 활용한다

#### 왜 사용하는가?

> 파이썬에서는 한 라이브러리에 대해 하나의 버저만 설치가 가능하나, 다양한 프로젝트를 만들며, 각각 다양하고, 종류가 다른 라이브러리를 사용하게 된다.
>
> 이 과정에서 호환성 문제 등 문제가 발생할 수 있어, 글로벌환경이 아닌 각각의 독립된 환경을 구축하게 된다.

- 가상환경 만들기

```sh
$ python -m venv 가상환경이름
```

가상환경이름은 특수한 상황이 아닌 이상 venv로 통일해준다

- 활성화하기

```sh
$ source 가상환경이름/Scripts/activate
```

enter 후 (가상환경이름) 나오면 활성화 완료

- 확인해보자

```sh
$ pip list
```

글로벌환경에서는 이전에 패키지까지 확인가능하나, 활성화되었다면 2개만 확인할 수 있다.

- 비활성화

```sh
$ deactivate
```

※ 가상환경의 이름은 같아도 상관없다. 폴더 위치만 중복되지 않으면 된다. 단 가상환경이 설정된 폴더의 위치는 함부로 이동시키지 않아야한다.



#### vscode에서 가상환경 만들기

위의 과정을 수행하고 vs코드를 열어도, 가상환경이 반영되어있지않음을 확인할 수 있다.

이 경우 ctrl + shift + p -> Python Select interpreter -> python venv 버전을 눌러준 후 터미널을 새로 열면,  `$ source 가상환경이름/Scripts/activate` 이 자동으로 떠있는 것을 확인할 수 있다.



#### 가상환경에서 django

- django 설치

```sh
$ pip install django
```

가상환경은 라이브러리가 초기화되어있기 때문에 django를 다시 설치해야한다. 설치없이 프로젝트를 진행하면 글로벌환경에서 만들어지게 된다.

- 프로젝트 생성

```sh
$ django-admin startproject crud .
```

가상환경과 동일한 폴더에서 진행되어야하기 때문에 뒤에 `.` 을 붙인 후 생성한다

- 필요할 경우 패키지들을 추가해준다

```sh
$ pip install requests
$ pip install ipython django-extension
```



#### git으로 관리하기

이전과 동일하게 git init, remote, add, commit, push를 해준다.

다만 올리면 안되는 요소들에 주의해야한다.

`.vscode/` 

`venv` 가상환경으로, 용량이 매우 크다

`db.sqlite3` 공개되어서는 안되는 중요한 데이터베이스이다

이들을 제외하기 위해선 `git ignore` 을 이용한다

<a>https://gitignore.io </a>에서 os, ide, 언어, 프레임워크, 가상환경을 검색하여 나오는 문서들을 복사

프로젝트 폴더에 .gitignore 만들고 복사 후 저장하면 자동으로 필요없는 파일이 필터링된다





#### 패키지 관리

> 가상환경이 옮겨지지 않는다면, git clone 해도 패키지가 없어 정상구동이 되지 않는다.
>
> pip freeze 를 활용하여 현재환경에 설치된 패키지를 requirements 로 출력한다



- 패키지 요구사항 파일 생성하기

```sh
$ pip freeze > requirements.txt
```

requirements.txt 파일이 생성된 것을 확인할 수 있다.

가상환경에 패키지를 추가할 때마다 freeze 는 계속 해줘야한다. 여러번 해도 위에 덧씌워질 뿐, 중복 생성되지 않는다!



- git에 push된 패키지 요구사항 파일 다운 받기

```sh
$ git clone **
$ python -m venv
$ source venv/Script/activate
$ pip install -r requirements.txt
```

git에서 내려받은 후, 동일하게 가상환경을 생성해준 후 requirements 를 설치한다

※ clone시 주의사항 : makemigrations 는 생략 가능하나 `migrate`는 꼭 해줘야한댜



#### 초기데이터(initial data) 설정하기

fixture : django가 데이터베이스로 import 할 수 있는 데이터 모음

app을 처음 설정할 때 데이터베이스를 미리 채워야하는 상황이 존재하는데 이러한 초기데이터를 제공하는 방법 중 하나이다.



- dumpdata / 관리자정보

```sh
$ python manage.py dumpdata app_name.ModelName [--options] > fixtures name
$ python manage.py dumpdata auth.User --indent 4 > users.json
```

> json 파일이 생성된다. app directory 안에 fixtures 폴더 생성, 안에 appname 폴더 생성 후 넣어준다

- load data

```sh
$ python manage.py loaddata fixtures_path
```

