# 0724 python PJT_Sample

> 프로젝트란 일정한 기간 안에 일정한 목표를 제약조건하에 요구사항을 수행해 일정한 목적을 달성하는 것



- ### 요구사항

> 음악차트 페이지를 구성하기 위하여 데이터를 수집하는 단계입니다. 아래의 기술된 사항은 필수적으로 구현해야 합니다.

1. 데이터

   1) 제공되는 music.json 파일을 활용합니다.

   2) music.json은 '에잇' 정보를 가지고 있습니다.

   

2. 결과

   1) 제공된 데이터에서 singer, title 키에 해당하는 정보만 가져옵니다.

   2) 가져온 정보를 새로운 dictionary 로 반환하는 함수 music_info 를 완성합니다.



```python
music_json = open('data/music.json', encodinbg='UTF8') #open은 ('파일명', '형태') , data라는 폴더안에 music.json 폴더 오픈
# 형태란 비어있으면 자동으로 r -> 읽기전용 
# 그냥 재생시 오류날 수도 -> 오류 문구 구글링 해봐서 해결책 찾아봄. 현재는 encoding = UTF8 을 변경해야 정상 가동

import json
music_dict = json.load(music_json)
# music_dict 가 딕셔너리로 변형잘 되어있나는 type() 이용해서 확인

#여기까지 1. 데이터 끝

def music_info(music): # 함수선언
   #현재 원 폴더는 key : value가 6개 짜리. 그 중 필요한 정보 두개만 줍줍해야함
    result = {}
    result['singer(접근하고 싶은 key)'] = music['singer(접근하고 싶은 key)'] 
    result['title'] = music['title']
    #dictionary를 꺼내올 때는 []
    return result
    
print(music_info(music_dict)) # 함수 호출
{'singer' : 'IU', 'title' : '에잇'} 
#2. 결과
```

```python
# 위에꺼를 깔끔하게 
import json

def music_info(music):
    result = {}
    result['singer'] = music['singer'] 
    result['title'] = music['title']
    return result

#json파일을 불러오는 코드
music_json = open('data/music.json', encodinbg='UTF8') 
#json을 dict로 변환하는 코드
music_dict = json.load(music_json)
#music_dict 함수 실행
print(music_info(music_dict)
{'singer' : 'IU', 'title' : '에잇'} 
```

```python
# 심화, 요구사항이 추가됨. 파일 안에 []로 딕셔너리가 4개짜리 리스트가 들어가있는 상태
# 이전에는 데이터1개 일때, 이번에는 많을 때, 동일하게 각 딕셔너리별로 singer와 title을 꺼내온다
# 이전에 한 작업을 반복하는
import json
import pprint

def music_info(musics):
    result = []
    for music in musics:
        music_detail = {}
        music_detail['singer'] = music['singer']
        music_detail['title'] = music['title']
        # [] + [ {iu} ] => [{iu}]
        # [{iu}] + [ {조정석} ] => [{iu},{조정석}]
        result = result +[music_detail]
    return result
    
    
musics_json = open('data/musics.json', encoing='UTF8')
musics_list = json.load(musics_json)
# 프린트로 데이터 올바르게 들어갔는지 확인
# 그냥 보면 데이터량이 많아 보기 힘들지만, pprint를 이용하면 보기 편함
pprint.pprint(musics_info)
[{'singer' : 'iu', 'title' : '에잇'}, {'singer' : '조정삭'}, {'title' : '어쩌구'}, ....]

```

