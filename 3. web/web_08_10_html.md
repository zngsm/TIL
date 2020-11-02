# 0810 web



http://jsfiddle.net

can I use -> 브라우저 별로 사용할 수 있는 지 확인할 수 있는 사이트



## Html

> hyper text markup language 
>
> 웹 컨텐츠의 의미와 구조를 정의



`hyper text` => 과거 순차적으로 텍스트를 넘겨봤다면, 링크를 통해 원하는 페이지로 넘어갈 수 있도록 한다

`http` : `hyper text` transfer protocol 



`markup language` => 태그 등을 이용하여 문서나 데이터 구조를 명시하는 언어

프로그래밍 언어와는 다르게 단순하게 데이터를 표현하기만 한다



### 기본형식

```html
<!Doctype html> 문서 유형을 지정
<html lang="ko"> 언어 korean
<head> head 요소 문서 : 제목, 문자코드와 같이 해당 문서 정보를 담고있으며 브라우저에 나타나지 않음 css 선언 혹은 외부 로딩파일 지정 등을 입력한다
	<meta charset="UTF-8"> utf-8 로 인코딩
	<title> Document</title>
</head>
<body> -> 브라우저 화면에 나타나는 정보. 실제 내용
 
</body> 
</html>
```



### DOM 트리

document - html

html - head / body

head - title

title - my title

body - h1

h1 - p ..... -> 이와같이 태그들은 부모 태그, 자식태그로 나뉜다

이들 사이에선 2 spaces of 4spaces를 띄어줘야한다



### 요소

> 시작태그 - 컨텐츠 - 닫는태그 

"<h1> contents </h1>""



### 속성

"<a href="https://google.com"></a>"

`=` 공백없이, `" "` 사용

공통 속성이 있음

id, class, hidden, lang, style, tabindex, title, .... , 나중에 배울 예정



※ 크롬 개발자 도구 열기

ctrl + shift + i 

f11



naver.com 를 탐색해보자. 태그마다 div를 확인할 수 있다

div, span 로 표현되는 것에 의미를 부여하기 위해 시맨틱 태그 사용

-> 구글 뉴스에서 잘 사용되었음



### 시맨틱 태그 

총 13개. 아래 6개가 주요!

`header` 문서전체나 섹션의 헤더

`nav` 내비게이션

`aside` 사이드에 위치한 공간

`section` 문서의 일반적이 부분

`article` 문서, 페이지, 상태 안에 독립적으로 구분되는 영역

`footer` 문서 전체나 섹션의 푸터, 마지막 부분



- 장점

  1. 읽기가 쉬워진다(개발자 입장에서)

  - 개발자가 의도한 요소의 의미가 명확히 드러남
  - 코드의 가독성을 높이고 유지보수를 쉽게 한다

  2. 접근성이 좋아진다

  - 검색엔진 -> 시력장애용 스크린리더 -> 더 나은 사용자 경험을 제공



### 블록- 인라인

> 자리를 차지하는 정도의 차이



- 블록요소 - 너비하나 전체를 차지. 그 다음 요소는 무조건 아래로
- 인라인 요소 - 옆에 다른 요소가 올 수 있음



### 문서 구조화

- text : 글자 입력

```html
<!--제목표시하기-->
<hn> n의 숫자는 1~6까지이며 1이 제일 크고 6이 제일 작은 제목의 크기이다</hn>

<!--단락 만들기-->
<p>
    paragraph 의 약자로, 텍스트 표시할 때 가장 많이 ! 줄 바꿈 없이 한 줄로 표현됨
    단, 텍스트 줄이 브라우저 창의 너비보다 길어진다면 줄이 자동으로 바뀌다
</p>

<!--줄 바꾸기-->
<br> break의 약자

<!--수평줄을 넣어 분위기 전환-->
<hr> horizontal의 약자

<!--굵게 표현하고 싶다면-->
<b> 굵게 표시되는 텍스트 </b>
<strong> 굵게 '강조'할 텍스트 </strong>

<!--이탤릭체로 표현하고 싶다면-->
<i> 이탤릭체로 표시된다 </i>
<em> 이탤릭체로 '강조' 된다 </em>

<!--단순히 영역을 묶고 싶다면-->
<span> 자체로는 의미가 없으나, 일부 텍스트만 묶어 스타일 적용을 위해 사용된다 </span>
```



- list : 목록 만들기

```html
<!--순서가 없는 목록 만들기-->
<ul>
    <li> 내용 </li>
    <li> 내용 </li>
</ul>

<!--순서가 있는 목록 만들기-->
<ol> <!-- 순서의 type="" 지정해주고, start=""를 통해 시작 범위를 알려줄 수 있다 -->
    <li> 첫번째 내용 </li>
    <li> 두번째 내용 </li>
</ol>
```



-  table : 표 만들기

```html
<!-- 기본 표 생성하기 table, 행 만들기 tr, 행마다 셀 만들기 td 제목 만들기 th-->
<table> <!-- 표 생성 -->
    <tr> <!-- 행 만들기 -->
        <th> 제목 셀 </th>
        <td> 내용 </td> <!-- 행마다 셀 만들기 -->
        <td> 내용 </td>
    </tr>
    <tr>
        <th> 제목 셀 </th>
        <td> 내용 </td>
        <td> 내용 </td>
    </tr>
</table>

<!-- 표에 제목 붙이기 -->
<table>
    <caption>
        <p>
           여기에 제목!
        </p>
    </caption>
    <tr> <td> 이하 동일하게 표 만들기!</td></tr>
</table>

<!-- 표 구조 정의하기 -->
<table>
    <thead> <!-- 표의 제목 부분 -->
    	<tr>
            <td></td>
        </tr>
    </thead>
    <tbody> <!-- 표의 본문 -->
    	<tr>
            <td></td>
        </tr>
    </tbody>
    <tfoot> <!-- 표의 요약 부분 -->
        <tr>
        	<td></td>
        </tr>
    </tfoot>
</table>

<!-- 셀 병합하기 -->
<td colspan="합칠 셀 개수- 가로로"> 내용 </td>
<td rowspan="합칠 셀 개수- 세로로"> 내용</td>

<!-- 여러 열을 묶어 스타일 지정 '4열 중 2, 3열에 검정색, 4열에 파란색 지정하는 경우' -->
<table>
    <colgroup>
        <col> <!-- 1열은 아무런 속성없기 때문에 비워준다 --> 
        <col span="2" style="backgroundcolor : black;"> <!-- 2, 3열은 같은 속성이기 때문에 span으로 묶어서 선언해준다 -->
        <col style="backgroundcolor : blue;">
    </colgroup>
</table>
```



- image : 이미지

```html
<!-- 이미지 삽입 -->
<img src="동일폴더는 파일명만, 하위폴더는 /하위폴더/파일명" alt="이미지 설명해주는 텍스트">

<!-- 이미지 크기 조절 -->
<img src"" alt"" width="" height="">

<!-- 이미지에 설명 글 붙이기 -->
<figure>
    <img src="">
    <figcaption> 이것은 이미지의 설명입니다 </figcaption>
</figure>
```



- link : 하이퍼링크

```html
<!-- 링크 만들기 -->
<a href="링크주소"> 텍스트로 표현하면, 텍스트만! 이미지면 여기에 img 코드를 넣어준다 </a>
```



- Form : 폼 만들기 -> 로그인, 회원가입 창 등

```html
<!-- 기본 폼 만들기 -->
<form method="서버에 어떻게 넘겨줄 것인가" name="폼들을 구분하기 위한 이름" action="해당 내용을 처리할 서버상의 프로그램" target="action에서 지정한 파일을 다른 위치에서 열도록 지정">
    폼 만들기!
</form>

<!-- action -->
<form action="어디로 보낼 것인가?">
    naver 검색창 form의 경우 action = /search
</form>

<!-- method -->
<form method="get">
    get은 입력값이 주소표시줄에 표시된다
</form>
<form method="post">
    post 는 입력값이 표시되지 않는다
</form>

<!-- 검색하기 -->
<form action="/search" method="get">
    <input type="text" title="검색">
    <input type="submit" value="검색">
</form>
```

> `method` : get 과 post를 받는다
>
> `get` : 주소표시줄에 사용자의 입력내용이 표시된다
>
> `post` : 대부분 사용되는 방식으로, 입력 내용의 길이 제한이 없으며 입력한 내용이 드러나지 않는다



- input  : 사용자 입력 받기

```html
<!--기본 입력 항목 만들기 -->
<input type="text">

<!-- 여러 번 폼이 사용될 경우 입력값 구분하기 -->
<input type="text" id="구분할 아이디">

<!-- 비밀번호 입력받기 -->
<input type="password">

<!-- 입력요소의 캡션 만들기 -->
<label for="id 와 연결되는 값"> 캡션 지정 </label>
<input type="text" id="label 과 input 값을 연결하기 위해 지정해주는 값">

<!-- 기타 속성 -->
<!-- 입력커서 자동표시 -->
<input type="type" autofocus>

<!-- 입력커서 내에 힌트표시하기 -->
<input type="type" placeholder="입력창에서 지시하고 싶은 내용">

<!-- 필수 입력 요소 설정하기 -->
<input type="type" required>
```



### 실습

```html
<!Doctype html>
<html>
    <head>
        <meta charset="UTF-8">
        <title> 실습 </title>
    </head>
    <body>
        <header>
            <img src="이미지" alt="이미지">
            <h1> 제목 </h1>
        </header>
        <section>
            <form>
                <div>
                    <label for="name"> 이름 : </label>
                    <input type="text" id="name" autofocus>
                </div>
                <div>
                    <label for="choice"> 여러개 박스 중 선택하기 </label> <br>
                    <select name="choice" id="choice">
                        <option value=""> 기본 선택창 </option>
                        <option value="1"> 1 - 이건 그저 표시되는 거, </option>
                        <option value="2"> 2 - 서버로 넘어가는 것은 value</option>
                    </select>
                </div>
                <div>
                    <p> radio 박스로 선택하기 </p>
                    <input type="radio" name="choice" id="1" value="1">
                    <label for="1">첫번째꺼</label>
                    <input type="radio" name="choice" id="2" value="2">
                    <label for="2"> 두번째꺼</label>
                </div>
                <input type="submit" value="제출버튼 입력칸">
            </form>
        </section>
        <footer>
            맺음말
        </footer>
    </body>
</html>
```







## CSS

> cascading style sheets



cascade -> 떨어져내리는



### 왜 배움?

> html 로는 스타일이 구림 스타일, 레이아웃을 설정



### style

```css
h1 /* 선택자*/ { /* 이하 적용할 스타일 나열*/
  color : blue; /* 속성 : 속성값 ; 으로 선언한다*/
  font-size: 15px;
}
```



### 선택자

- 기초선택자

```css
/* 전체선택자 : 모든 요소에 스타일을 적용시킨다 */
* {
    속성 : 속성값;
}

/* 태그 선택자 : 특정 태그가 쓰인 모든 요소에 스타일을 적용시킨다 */
p {
    font-size : 12px;
}
h1, h2 {
    text-align : center;
}

/* 클래스 선택자 : 특정 부분에만 스타일을 적용시킨다*/
.blue {
    color : blue;
}
/* html */ 
<p class="blue">

/* id 선택자 : 클래스 선택자와 비슷하나, 단 한번만 적용하기로 약속되어있다 중복 사용해도 에러발생은 아니지만 쓰지않는다 */
#purple {
    color: purple;
    }
/* html */ 
<p id="purple">

/* 속성 선택자 */
h1[title] {
    color : red;
}
input[type="text"] {
    color = black;
}
/* html */
<h1 title="">여기에만 적용</h1>
<input type="text">
```



- 고급선택자 : 다양한 중복되는 태그 중 특정 영역에 있는 태그만 선택하고 싶다면 

```html
<!-- 자식선택자 : 바로 하위의 태그만 지정하고 싶다면-->
.box > p {
	font-size : 30px;
}
<!-- 자손선택자 : 하위의 태그 전체를 지정하고 싶다면-->
.box p {
    font-color : blue;
}
<!--html-->
<div class="box">
  <div>
    <p> 얘는 자식선택자는 아닌 자손선택자 </p>
  </div>
  <p> 얘는 자식선택자이며 자손선택자이기도 하다 </p>
</div>
```



- 네이버의 선택자 경로로 확인해보자

```html
#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(1) > a
```

#NM_FAVORITE 라는 id 선택자에서

div 의 하위에 있는 group_nav 클래스

ul 리스트에서 list_nav와 NM_FAVORITE_LIST 라는 클래스 2개

li 리스트의 :nth-child(1) 첫번째 자식 선택자의 a 클라스를 의미한다





### css정의방법 

1. 인라인

```html
<h1> style="color:blue; font-size:100px;" </h1>
```

2. 내부 참조

```html
<head>
    <style>
    	h1 {
			color : blue;
			font-size: 20px
        }
    </style>
</head>
```

3. 외부참조

```css
.css /* 파일 따로 생성하여 */
h1 {
	color : blue;
	font-size: 20px
}
/* 를 적고
본 html 파일에 link로 추가 */
```

```html
<head>
    <link rel="stylesheet" href="외부 스타일 파일 경로">
</head>
```



#### 무엇이 가장 일반적인가?

> 외부참조가 가장 일반적이다
>
> 내부참조는 해당 html 파일 안에서만 style을 적용할 수 있으나,
>
> 외부참조의 경우 style 형식을 지정해둬 다른 html 파일에도 적용이 가능하다





### css 우선순위

`!important` -> 최상위 우선순위

`인라인`  - <style="">

`id` 선택자 - # {}

`class` 선택자 - . {}

`속성` 선택자 - 태그[속성] {}

태그 선택자 - 태그 {}

소스 순서 - 가장 아래것을 적용한다!



### css 크기 단위

- (상대)크기 단위
  - px(픽셀) -> 모니터 화소수에 따라 px 다 다름
  - & (백분율) ->  가변적인 구조 짤 경우
  - em 배수단위 - 부모 사이즈 기준 배수 단위 ( 부모에 사이즈 지정되어있으면 중복되어 지정될 수 있다)

  - rem 최상위 요소의 사이즈를 기준으로 배수단위 -> 일반적으로 더 많이 씀



### 색상단위

- 색상키워드

- rgb색상

- hsl 색상



### 문서표현

- 텍스트
- 컬러, 배경
- 목록꾸미기
- 표 꾸미기



### Box model

![image-20200817144631070](C:\Users\qbw00\AppData\Roaming\Typora\typora-user-images\image-20200817144631070.png)

- margin : 테두리 바깥의 외부 여백; 배경색 지정 불가
- border : 테두리 영역
- padding : 테두리 안쪽 여백 ; 배경색, 이미지가 적용된다
- 이하 실제 콘텐츠 영역

```html
<!-- 둘은 같다 -->
.border {
  border-width: 2px;
  border-style: dashed;
  border-colo: black;
}

.border { 
  border : 2px dashed black;
}
```



#### box sizing

- content box  : 가장 기본 형태로 굳이 추가로 입력할 필요가 없다. box의 너비를 정할때 내부 content의 크기가 지정된다. padding, margin 너비가 넓어질 수록 전체 크기는 커지게 된다
- border box : border(실제로 보이는 박스의 크기)를 기준 사이즈로 한다

```html
.box-sizing {
  box-sizing : border-box;
}
```



#### margin collapsing

인접 형제 요소간의 marigin 은 큰 값으로 덮어써진다.



### display

- display : block
  - 화면 크기 전체의 가로폭을 차지하며, 줄 바꿈이 발생한다
  - 블록 안에 인라인을 넣을 수 있다.
  - div / ul, ol, li / p / hr / form 등

```html
<!-- 왼쪽 정렬 -->
margin-right : auto;
<!-- 오른쪽 정렬 -->
margin-left : auto;
<!-- 중앙 -->
margin-right : auto;
margin-left : auto;
```

- dispaly : inline
  - content 너비만큼 가로폭을 차지하며, 행의 일부요소로 줄 바꿈이 일어나지 않는다
  - 박스 개념이 아니기 때문에 width, height, margin, padiding 등의 값을 지정불가하며 상하여백을 만들고 싶다면 line-height로 지정 가능하다
  - span / a / img / input, labe; / b, em, strong, i 등

````html
<!-- 왼쪽 정렬 -->
text-align : left;
<!-- 오른쪽 정렬 -->
text-align : right;
<!-- 중앙 -->
text-align : center;
````

- display : None
  - 해당 요소를 화면에 표시하지 않는다. 공간조차 사라진다. 
  - 아래 박스가 있었다면 아래 박스가 위로 올라오게 된다는 것. 단순히 안보이는것과는 다름 => 다른 레이아웃 배치구조를 망칠 수 있음 ㅠㅠ

- visibility: hidden 공간은 차지하나 화면에서 표시만 하지 않는다



### css position

- static : 디폴트값, 기준위치(좌측상단)

- 좌표 프로퍼티 를 사용하여 이동 가능 (top bottom left right)
  - relative(상대위치) : static 위치를 기준으로 이동
  - absolute(절대위치) : static 이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동

  - fixed(고정위치) : 부모 요소와 관계없이 브라우저를 기준으로 이동. 스크롤시에도 항상 같은 곳 위치



- html 문서는 `mdn` 서류로 확인하기
- html 빠른 코딩을 위한 오픈소스 `emmet`에서 확인하기
- 브라우저 사양별로 웹 구동 가능한지 확인 `can I use`