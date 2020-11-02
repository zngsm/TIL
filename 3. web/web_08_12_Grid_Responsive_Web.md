## 0812 Grid / Responsive Web



### css layout

>  웹 페이지에 포함되는 이요소들을 취합하고, 어느 위치에 놓일 것인지를 제어하는 기술

display, position, float, flexbox, grid ... 등



### float

> float된 이미지 좌, 우측 주변으로 텍스트를 둘러싸는 레이아웃을 위해 도입

- 기본값 : none
- float : left; 요소를 왼쪽으로 
- float : right ; 요소를 오른쪽으로



#### 실습

- lorem -> 랜덤 단어

- float

해당 클래스를 적용하여 왼쪽으로 이동시켜보자.

```html
.left {
      float : left;
    }
```

이미지가 두개 겹쳐진다면?

- float clear

부모 태그 다음에 (::after) 가상의 빈 블락을 만들어서 겹치지 않게 하자.

```python
.clearfix::after {
      content : ""; # 내용이 비어있다
      display : block; # block 으로 아래에서 올라오지 못하게
      clear : both; # clear : left -> 왼쪽에서 오는 float를 초기화하겠다,  float left와 right (both)
    }
```



### flex box

> 요소간 공간 배분과 정렬 기능을 위한 1차원(단방향) 레이아웃



- 요소와 축

  - flex container - 부모요소

  - flex item - 자식요소
  - main axis - 가로축

  - cross axis  - 세로축

![image-20200812134940877](C:\Users\qbw00\AppData\Roaming\Typora\typora-user-images\image-20200812134940877.png)

- 시작은 부모에 선언하기

```html
.flex-container {
	display : flex;  # block이 된다
	display : inline-flex;  # 내부에 인라인 정렬 가능한 block
}
```



- 속성 설정하기
  - flex-direction 메인축 방향 변경
  - main axis 방향만 바뀜
  - flex는 단방향 레이아웃 
  - row (default) 오른쪽 정렬 ->
  - row-reverse 왼쪽으로 정렬 <-
  - column 아래로
  - column-reverse 위로



- 메인축 방향 정렬 justify-content 

- 교차축 방향 정렬

  - align-items 교차축 기준 한 줄

  - align-self 골라서 한 줄

  - align-content 여러줄



- content 는 여러줄

- items 한 줄

- self 하나만 선택해서,,



실습

기본 flex-container 실행했을 경우

기본 방향 row -> 로 흘러간다



item 은 행으로 나열된다

메인축의 시작선에서 시작된다

크로스축의 크기를 채우기 위해 늘어난다 -> stretch





margin 0 auto -> 상하는 0 좌우는 균등분배 => 가운데 정렬



Bootstrap

빠른 디자인, 반응형, 프론트엔드 오픈소스, 반응형 그리드시스템, 미리 만들어진,,

부트스트랩으로 만든 사이트 -> 넷플릭스, 보그 가 대표적이다

 

language 코드!! 한국 ko 영어 en 중국 cn





bootsratp -> bootstrap min (1만줄짜리는 한줄로! 조금 더 빠르게 구동된다)



css는 link로 javascript 는 body 태그 마지막 전줄에 script 로 불러온다





css 노말라이즈 -> 부트스트랩 리부트 파일에 있음

표준화로 지정



reset

공격적인 방법

-> 웹 표준스탈을 가는게 아닌, 자체 스타일 다 없앤다는 의미

normalize

젠틀한 솔루션

-> 웹 표준에 맞추는 것.

개발전에 리부트를 하고 시작하기! 웹이 빠르게 발전되니 검증된 곳에서 받아 쓰자!



rem ->root 기준 html 16px => 16 * 0.25 = 4 px

.mt-1,

.my-1 {

margin-top : 0.25rem !important}



.mx-0

좌우 -> 마진 왼쪽 오른쪽이 0 이라는 것!



.mx-auto

수평 중앙 정렬



.py-0

패딩 상하를 0으로 주겠다는것,,!



.bg-"class"

배경색 만들어주는 것!

실습



반응형 웹

다양한 디바이스 -> one source로 다양한 디바이스에 적용하자!

일일이 하기엔 너무 번거로움



부트스트랩의 그리드시스템을 이용해보쟝 ㅎ



12개의 column -> 약수가 많음



실습 06



오늘 라이브에서 무엇을 배웠나요?

position

float -> 위로 띄워서 그 주변으로 인라인스타일, 텍스트스타일이 감싸는 레이아웃 형태를 위해 태어났다

이것만으로는 좀 힘들었다.

그래서 flexbox가 떠오름 

아이템과 공간배분을 강력한 정렬을 위해 탄생한 1차원 정렬 모델

반응형 웹 디자인

그리드시스템 가져다가 사용





component

```html
class="btn btn-primary"
```



col-n

> 기본값 설정! 

col-lg-3

> 라지보다 클때 해당 너비 지정! 만약 위의 기본값 없을 경우 라지보다 작을때는 줄 자체가 바뀌어버림;;;;; col 설정이 없는거라서