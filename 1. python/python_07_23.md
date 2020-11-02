# 함수

> input(`x`) -> Function `f:` -> output `f(x)`

특정한 기능을 하는 코드의 묶음

가독성, 재사용성, 유지보수의 편리성을 위해 사용된다.



## 함수의 선언과 호출

선언 : `def f(x):` 다음 `4space` 들여쓰기로 코드블록 생성

호출 : `func()` or `func(val1, val2)`

매개변수를 넘겨줄 수 있으며, `return` 을 통해 결과값을 전달할  수 있다.

return 하지 않으면 `None`을 반환한다

```python
# 내장함수 목록 확인
print(__builtins__)
dir(__builtins__)
```



## 함수의 Output

함수의 `return` 으로 어떠한 종류여도 상관 없다. 단, 오직 한 개의 객체만이 반환 가능하다.



# 함수의 입력(Input)



## 매개변수(parameter) & 인자(argument)

### (1) 매개변수(parameter)

```python
def func(x):
      return x + 2
```

> `x`
>
> 함수 내부에서 활용할 변수 -> 함수 정의에서 확인 가능

### (2) 전달인자(argument)

```python
func(2)
```

> `2`
>
> 실제 전달되는 입력값 -> 함수의 호출에서 확인 가능



## 함수의 인자

입력값으로 `인자(argument)` 넘겨줄 수 있다



### 위치 인자 (Positional Arguments)

> 함수는 인자를 위치로 파악한다

`x` 와 `y`의 값이 바뀌면, `result` 도 다르게 반환된다

```python
def f(x, y):
    result = x - y
    return result
```



### 기본 인자 값 (Default Argument Values)

> 인자 없이 기본 값을 설정할 수 있다
>
> 기본값 '익명' 호출시 인자가 없으면 기본 인자값이 활용된다
>
> 단, 기본인자값을 가지는 인자 다음에 기본값 없는 인자는 불가 `{name='anony', age}` = error

```python
def greeting(name='익명'):
    return f'{name}, 안녕?'
```



### 키워드 인자 (Keyword Arguments)

> 직접 변수 이름을 특정 인자로 전달

```python
def greeting(age, name='익명'):
    return f'{age}세 {name}님 환영합니다'
greeting(20, '홍길동')
greeting(age=20, name='홍길동')
greeting('name='홍길동, age=20')
```



## 정해지지 않은 여러 개의 인자 처리

`print`(**objects*, *sep=' '*, *end='\n'*, *file=sys.stdout*, *flush=False*)

`sep=''` 은 print(a,b) 에서 a와 b 간의 구분 기본은 ' ' 공백

`end=''` 은 print(a,b) 출력 후 끝 기본은 /n 다음 줄로

`file=` 은 출력의 버퍼링 여부 결정 write(string) 메서드를 가진 객체여야함. 기본이거나 None은 sys.stdout 사용

`flush=` 는 키워드 인자가 참일 경우 스트림이 강제로 풀린다

### 가변(임의) 인자 리스트(Arbitrary Argument Lists)

> `*args` : 임의의 개수의 위치인자를 받는다 ( 매개변수 목록의 마지막)

`print()` 와 같이 개수가 정해지지 않은 임의의 인자를 받아내기 위해서 사용

`turple` 형태. 매개변수에 `*` 로 표현

```python
def func(a, b, *args):
```



### 가변(임의) 키워드 인자(Arbitrary Keyword Arguments)

> `**kwargs` : 임의 개수의 키워드 인자를 받음

`dict` 형태로 처리가 되며 `**`로 표현가능하다. 보통 `kwargs` 사용, `**kwargs` 로 받아 처리

```python
def func(**kwargs):
```



# 함수와 스코프(scope)

> 함수가 생성하는 코드 내부의 공간(scope)

함수로 생성된 공간은 `지역 스코프(local scope)`이며, 그외의 공간은 `전역 스코프(global scope)`

- **전역 스코프(`global scope`)**: 코드 어디에서든 참조할 수 있는 공간
- **지역 스코프(`local scope`)**: 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간

- **전역 변수(`global variable`)**: 전역 스코프에 정의된 변수
- **지역 변수(`local variable`)**: 로컬 스코프에 정의된 변수



## 이름 검색(resolution) 규칙

> `LEGB Rule` : 사용된 이름(식별자)들이 저장된 이름 공간, 아래이 순서로 이름을 찾아간다

- `L`ocal scope: 정의된 함수

- `E`nclosed scope: 상위 함수

- `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈

- `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성



### 변수의 수명주기(lifecycle)

- **빌트인 스코프`(built-in scope)`**: 파이썬이 실행된 이후부터 영원히 유지

- **전역 스코프`(global scope)`**: 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 인터프리터가 끝날때 까지 유지

- **지역(함수) 스코프`(local scope)`**: 함수가 호출될 때 생성되고, 함수가 가 종료될 때까지 유지 (함수 내에서 처리되지 않는 예외를 일으킬 때 삭제됨)



# 재귀 함수(recursive function)

> 자기 자신을 호출하는 함수



## 반복문과 재귀 함수의 차이

- 자기 자신을 호출하는 재귀함수는 알고리즘 구현시 많이 사용된다.
- 코드가 더 직관적이고 이해하기 쉬운 경우가 있다.
- 팩토리얼 재귀함수를 [Python Tutor](https://goo.gl/k1hQYz)에서 확인해보면, 함수가 호출될 때마다 메모리 공간에 쌓이는 것을 볼 수 있다.
- 이 경우, 메모리 스택이 넘치거나(Stack overflow) 프로그램 실행 속도가 늘어지는 단점이 생긴다.
- 파이썬에서는 이를 방지하기 위해 1,000번이 넘어가게 되면 더이상 함수를 호출하지 않고, 종료된다. (최대 재귀 깊이)
- 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용한다.
- 재귀 호출은 `변수 사용` 을 줄여줄 수 있다.

