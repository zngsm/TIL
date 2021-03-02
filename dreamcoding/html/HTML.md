# HTML

> hyper text markup language

```html
<recipe>
  <title> 제목 </title>
  <ingredientlist>
  	<ingredient> 재료 </ingredient>
  </ingredientlist>
  <preparation>
  	준비요소
  </preparation>
</recipe>
```

[jsbin.com](www.jsbin.com)



### html 구조

```html
<html>
    <head>
        <meta charset="utf-8"> <!-- 글자의 set은 utf-8 준수 => 현존하는 모든 언어-->
        <meta name="viewport" content="width=device-width">
        <title></title>
    </head>
    <body>
        user에게 실제 보여지는 부분
        <h1>
            제목 제일 큰 제목
        </h1>
        <h2>
            그 다음 큰 제목 ... h6까지 있습니다 ^^
        </h2>
        <button>
            누를 수 있는 버튼
        </button>
        <randomRandom>
        	이렇게 써도 나온다고.....???
        </randomRandom>
    </body>
</html>
```

> MDN 사이트 https://developer.mozilla.org/ko/docs/Web/HTML
>
> `randomRandom` 브라우저는 에러 발생시 -> 에러를 예측해서 회복하여 html 파일을 정상적으로 read 가능함(비정상적 태그를 써도 표시되는 이유)

### W3C

> 웹 표준화 기관 => HTML 태그에 맞게 브라우저들이 구현된다.



### body 내의 태그

![image-20210302195525019](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210302195525019.png)

- header
- nav
- sidebar
- main
- footer



### BOX & ITEM

- Box
  - header
  - footer
  - nav
  - aside
  - main
  - section
  - article
  - div
  - span
  - form
- item
  - a
  - button
  - input
  - label
  - img
  - video
  - audio
  - map
  - canvas
  - table



### Block & Inline

- Block
  - 블록 엘리멘트는 공간이 확보되어도 한줄당 하나씩만 들어간다.
- inline
  - 인라인은 공간이 확보될 경우 다른 태그 옆에 배치가 가능하다.



### example

```html
 <!-- BOX -->
  <header></header>
  <footer></footer>
  <section></section>
  <div></div>
  <span></span>
  
  <!-- ITEM -->
  <h1></h1>
  <button></button>
  
  <!-- a -->
  <a href="https://google.com" target=_blank>Click</a>
  <!-- target에 따라 _self 는 현재창 _blank 는 새창-->

  <!-- block inline -->
  <p>this is a sentence. <b>That</b> is ...</p>
  <p>this is a sentence. <span>That</span> is ...</p>
  <p>this is a sentence. <div> That </div> is </p> <!--줄바꿈 div는 블록이다-->

 <!-- ol ul li-->
  <ol type="I" reversed>
    <li>1</li>
    <li>2</li>
    <li>3</li>
  </ol>

  <ul>
    <li></li>
    <li></li>
    <li></li>
  </ul>

 <!-- input -->
  <label for="input_name">Name:</label>
  <input id="input_name" type="text">
  <!-- password, color, file, button 등 다양한 type 이 존재한다 -->
```





### 시맨틱 태그

![image-20210302195547697](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210302195547697.png)

