# README_Sample

> 프로젝트 완료 후 README 와 함께 lab.ssafy.com 에 제출한다



## vscode 에서 git 관리

> 현재 위치 확인하기. git은 시행한 폴더의 하위 폴더까지만 반영. 상위일 경우 반영이 불가하다
>
> vs code에서 terminal - `ls` 명령어를 통해 해당 폴더와 그 안에 파일들을 확인할 수 있다.
>
> git 을 쓰는 이유, `버전관리`와 `협업`을 위해

1단계 `working dir`ectory  : 내가 작업한 파일들

2단계 staging area : 그 파일들을 올리는 곳

3단계 local repo (.git) : 그 파일을 이 곳에 저장. .git 에 작업한 파일들 들어감

4단계 원격저장소 : git lab

```sh
햣 $ ls
# 현재 폴더 안에 파일 확인가능
$ ls -a
# 숨김파일까지 확인 가능
$ git in it
# .git 이라는 빈 폴더 만들었다 -> 이 안에 나의 데이터가 쌓이며 버전을 관리할 수 있다.
# 만약 두 번쓰면? 이미 있어서 -> 다시 생성했습니다. 첫 단계에서만 딱 한번 하면 된다.
$ git add .
# 1단계 파일을 2단계로 넣는것. 개별 파일 이름을 적을 수 있음. 근데 다 넣기 귀찮음. `.` 만 적으면 해당 폴더 전체파일을 의미
$ git config --local user.name  / user.email 
# global은 전체에 적용, local은 이 폴더만!
$ git commit -m ""
# 2단계 -> 3단계 새로운 데이터를 저장. 나의 버전을 새로 쌓아가는 것. 그럼 왜 버전을 수정했는지? 설명을 적어줘야함
# -m 메세지의 약자 " " 내가 넣고 싶은 메세지를 입력

# 원격 저장소에 업로드해야하는데 어디에 할 것인지를 알려줘야함
# git lab에서 newproject 생성 name : pjt01 로 만든다 -> 원격 저장소가 생성된다.
# clone 에서 http url 따기
$ git remote add origin url
# git아, remote(원격저장소 기능에서 추가할 건데) origin 이라는 별명을 추가할게 실제 주소는 url이야 라는 뜻.
# 최초 한번만 시행
$ git push origin master
# 3단게 -> 4단계, origin 에 master를 넣을거야! master = 내가 올린 커밋들의 기록이라 생각하면 편함
# 사용자 이름(id), 암호 나옴
# 비밀번호 잘못쓰면 access denied 나옴
# window 자격증명에서 gitlab 데이터 지우고 다시 시행해야한다

# 4단계까지 저장된 파일을 pc로 땡겨오려면?
# project 에서 clone - https url 복사
# c:/사용자/qbw00 -> 우클릭 -> git bash
$ git clone url(shift + insert 로 붙여넣기 가능)
# 생성완료! 

#생성된 깃랩 new project -> settings -> members -> invite member 로 교수님 추가하고 maintainer 로 add 하면 됩니당
```

lab.ssafy.com/ssafy4/projects

```sh
# 쓸데없는 파일 제외하고 싶을때
newfile - .gitignore 생성
포함되면 안되는 파일/
파일
-> git bash 실행
$ git status
git ignore와 원래 업로드 파일들만 나오게 됨
그리고 업로드 진행 ^~^
```

```sh
$ git init 한 것을 취소하고 싶다면?
# 숨김파일 .git 삭제해야함
$ rm -rf .git 
# 삭제 완료. 삭제하시겠습니까? 이런거 안물어보니 *주의*
```





## 0724_python PJT

> project01 을 진행하면서 새롭게 배운 것들, 에러를 해결한 것들을 정리합니다.
>
> 형식은 나만의 자유형식으로, 이하 예시입니다



## 새롭게 배운 것

- open()
  - filename : 내가 열고 싶은 파일의 이름을 적는다
  - mode : `r` 읽기모드, `w` 쓰기모드, 아무것도 적지 않으면 기본적으로 `r`로 적용된다
  - encoding : `UTF8` 한글때문에 파일이 정상적으로 dict로 변환이 안된경우 적용하여 해결가능

```python
open(filename, mode)
```



- Json
  - 아직은 뭔지 잘 모르지만, dict라고 생각하자

```python
import json
# json 데이터를 python에서 사용할 수 있는 dict 데이터로 변환
json.load
dict_dat = json.load(json_data)
```



