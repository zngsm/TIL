# Javascript: JS 기초

> 동적 프로그래밍을 위해 사용



## js intro

- 팀 버너스비

> www / http /uri 의 창시자, 현재 웹의 근간을 만들다



- 브랜던 아이크

> java script 설계자(놀랍게도 java와는 관련이 없다 😅😅)
>
> HTML 은 정적 -> 이를 동적으로 표현하기 위해 언어 도입을 결정



- 브라우저 전쟁 -> 파편화
- 모든 브라우저에서 동일하게 동작하기 위한 표준의 필요성 제기
- `ECMA 인터내셔널`에 기술규격을 제출한 이후 표준 제정에 대한 논의 지속



- `JQuery`
  - 라이브러리의 한 종류
  - jquery가 제공하는 API 사용시, 해당 툴 안에서 어떤 브라우저든 알아서 적용해준다(!!)



- 지금은? 표준화가 많이 진행되어 JQuery 없어도 가능해졌다
- 순수한 JS > `Vanilla JavaScript`



브라우저에서 부엇을 할 수 있는가?

- DOM (Document Object Model)
  - 문서(HTML) 조작
- BOM 조작
  - 브라우저를 object로 조작하는 것(일단 패스!)
- JavaScript Core
  - 자료구조를 포함한, 조건/반복/함수 ... 등!





## DOM (Document Object Model)

> 웹 페이지 문서 구조를 표현함으로써 스크립트 및 프로그래밍 언어와 페이지를 연결
>
> 문서를 논리 트리(DOM 트리)로 표현.
>
> 각 노드는 객체.
>
> DOM 메서드를 활용해 프로그래밍 트리에 접근 가능하다



- 브라우저의 기본적인 논리
  - `html` 문서를 받는다
  - `parsing`(구조화해석)한다
  - 구조화된 html을 `styling` 한다
  - style 요소가 끝나면 `lay out` 에 맞춰 배치한다



- 조작
  - 선택 `무엇을?` -> `selection`
  - 조작 `어떻게?` -> Manipulation



## Selection

- 단일 Node
  - document.getElementByid(id) <- id를 통해서만 불러올 수 있따
  - document.querySelector(selector) > id, class, 복합, tag 선택자 등 다 가능!
    - querySelector() > 하나만!
    - querySelectorAll() > 여러개!
- HTML collection(live)
  - document.get`Elements`ByTagName(tagName) 
  - document.getElementsByClassName(tagName)



## Manipulation

- innerText

  - Text 값을 넣어준다

  ```html
  innerText(<p>안녕하세요</p>)
  > <p>안녕하세요</p>
  ```

- inner HTML

  - html 요소를 그대로 집어 넣음 (XSS(해킹) 공격에 취약점 있으므로 주의)

  ```html
  innerHTML(<p>안녕하세요</p>)
  > 안녕하세요
  ```

- createElement

  - 아예 값을 추가한다!

- console.log('')
  - python의 print와 같은 역할(웹 > 검사 > console에서 확인가능)





## Event

> <b>특정이벤트</b>가 발생하면, <i>할 일</i>을 등록하자
>
> `EventTarget`.addEventListener(<b>type</b>, <i>listener</i>)







## 실습

실습할 때 > 어떠한 논리구조로 작성될 지 생각하고 작성해보기







![image-20201012174723323](C:\Users\qbw00\AppData\Roaming\Typora\typora-user-images\image-20201012174723323.png)

![image-20201012174756171](C:\Users\qbw00\AppData\Roaming\Typora\typora-user-images\image-20201012174756171.png)