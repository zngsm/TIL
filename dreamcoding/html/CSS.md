# CSS



## 1. 의미, 정의

> cascading style sheet



- Author style : 우리가 지정한 스타일  없다면->UserStyle

- User Style : 유저가 직접 지정(다크모드) 없다면->Browser

- Browser : 브라우저에서 지정된 스타일 
- 이관계를 무시하는 건 !Important (하지만 최대한 쓰지말자)



## 2. 선택자

- `*` 모든 태그를 지정
- `Tag`의 이름 -> 해당 태그를 고르는 것
- `#`id -> 해당 아이디를 선택
- `.`class -> 클래스
- `:`  state : 태그 옆에 쓸 수 있다. (:hover)
- `[]` attribute => a[href="naver.com"] a 태그 중 href가 네이버인 애들만 고른다. 
- href^="naver" 네이버로 시작되는 애들 href$=".com" .com으로 끝나는 애들



## 3. 스타일링

- padding: border의 안쪽 padding: 상 우 하 좌 (시계방향) / 상하 좌우

- marign: border의 바깥

- border

  ![image-20210304002820450](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210304002820450.png)

- css reference에서 확인하기



## 4. Display

- block : 상자.한 줄에 하나 (div)
- inline:  물건.한줄에 여러개(span) ; 컨텐츠 자체만을 꾸며주는 요소로 내용물이 없으면 width, heigth이 있어도 적용되지 않는다
- 직접 display : block 을 넣으면 한줄에 하나 inline-block(상자)을 쓰면 한줄에 여러개가 들어가는 block 형태
- inline을 쓰면 위의 설명;; 



## 5. position

- static : 기본값 left, top: 20px 넣어주면 움직이지 않음
- relative : 내 아이템 기준해서 left, top: 20px 넣어주면 상대적 위치로 움직임
- absolute : 아이템이 담겨져 있는 상자 기준에서 움직임
- fixed: 웹 페이지 기준으로 left, top: 20px 넣어주면 움직임
- sticky: fixed와 비슷하나 스크롤링 되어도 해당 위치에 고정됨



## 6. FLEX BOX

- container
  - display `flex` -> flexbox를 쓰겠다
  - flex-direction -> `row` 기본값 왼쪽 -> 오른쪽 `row-reverse` 오른쪽 -> 왼쪽/ `column` 위에서 아래로 column-reverse 아래에서 위로
  - flex-wrap -> `wrap` 페이지가 작아지면 다음줄로 넘어감 wrap-reverse 는 위에서 반대 순서로 , `nowrap`은 아무리 작아져도 넘어가지 않음(기본값) 
  - flex-flow : flex-direction + flex-wrap // column nowrap
  - justify-content : 중심축에서 아이템 정렬하는 것, flex-start (기본값); flex-end(오른쪽 정렬/ column은 아래에서 위로), center : 정가운데 space-around:  박스를 둘러싼 스페이스를 만들어주는 것, space-evenly: 동일한 간격으로 넣어주는 것, space-between: 화면에 딱 맞게 정렬
  - align-items : 반대축에서 아이템 정렬하는 것, baseline: item 의 크기에 상관없이 텍스트를 균등하게 맞춰준다 center : 기본값의 경우 수직정렬
  - align-content: 반대축의 justify-content// space-between
- item
  - order : 기본값은 `0` 컨테이너 안에 순서를 바꾼다 자주 쓰지는 않는다.
  - flex-grow: 기본값 0, 1을 넣어주면, 해당 container에서 남은 칸의 너비를 채우려고 한다 숫자는 다른 아이템에 대한 비율
  - flex-shrink: 컨테이너가 작아졌을 때.. 숫자가 클 수록 더욱 작아짐
  - flex-basis:기본값 `auto` 위의 grow, shrink와 상관없이 컨테이너 크기에 따라 아이템을 %로 지정할 수 있음
  - align-self: align 배치할 때 아이템 하나만 배치하고 싶을 때 사용

![image-20210304004352180](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210304004352180.png)

> 중심축 가로축 

![image-20210304004404922](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210304004404922.png)

> 중심축 세로축





![image-20210304004509460](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210304004509460.png)

![image-20210304004516306](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210304004516306.png)



color-tool