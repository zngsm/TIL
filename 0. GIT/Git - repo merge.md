# Git - repo merge

> 두 가지 이상의 레포를 하나의 레포로 합칠 때



- 합칠 main repo `main`
- 합쳐질 repo `pjt1` `pjt2`

```sh
# main 레포 생성 후 
$ git init
$ git remote add origin 'url'
# 혹은 
$ git clone 'url'
$ cd main
# main 레포 파일을 로컬에서 생성

$ git remote add pjt1 ../pjt1 # 이하 pjt1 의 경로
$ git fetch pjt1
$ git merge --allow-unrelated-histories pjt1/master #마스터 branch 명을 넣으면 됨
$ git remote remove pjt1 # 원격저장소명 삭제

$ git remote add pjt2 ../pjt2
# .. 이하 동일
# merge 진행시 commit 창이 켜진다.

# 혹시나 폴더 구조를 변경한다면
$ git add .
# 변경없다면 이 과정을 생략하고
$ git commit -m 'merge pjt1/pjt2'
$ git push
```

