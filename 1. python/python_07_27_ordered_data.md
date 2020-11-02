## 데이터 구조(Data Structure)

> **Program = Data Structure + Algorithm**
>
> orderd data structure : 문자열, 리스트



### 1. 문자열(string)

> 변경할 수 없다 immutable
>
> 순서가 있다 orderd
>
> 순회가 가능하다 iterable



#### 1) 조회 / 탐색 method

- `.find(x)`

  - x의 첫번째 위치를 반환. 값이 없을 경우는 `-1` 을 반환

  ```python
  'ssafy'.find('y')
  >> 4
  'ssafy'.find('x')
  >> -1
  ```

- `.index(x)`

  - x의 첫번째 위치를 반환. 값이 없을 경우 오류가 발생

  ```python
  'ssafy'.index('y')
  >> 4
  'ssafy'.find('x')
  >> ValueError
  ```

  

#### 2) 값 변경

- `.replace(old, new[ , count])`

  - 바꿀 대상 글자를 새로운 글자로 바꿔서 반환. count 지정시 해당 갯수만큼 시행

  ```python
  'ssafy'.replace('y','i')
  >>'ssafi'
  'ssafy'.replace('s', 'd', 2)
  >>'ddafy'
  ```

- `.strip([chars])`

  - 공백제거, 특정문자 지정시 양쪽을 제거, 왼쪽제거`lstrip`, 오른쪽 제거`rstrip`

  ```python
  'ssafy samsungs'.strip('s')
  >>'afy samsung'
  'ssafy samsungs'.lstrip('s')
  >>'afy samsungs'
  'ssafy samsungs'.rstrip('s')
  >>'ssafy samsung'
  '  ssafy samsung  '.strip()
  >>'ssafy samsung'
  ```

- `.split()`

  - 문자열을 특정단위로 나누어, 리스트로 바꿈

  ```python
  inputs = input().split() # 5 3 입력시
  >> ['5', '3']
  'ss_a_fy'.split('_')
  >>['ss', 'a', 'fy']
  ```

- `'separator'.join(iterable)`

  - 특정 문자열로 만들어 반환
  - 반복가능한 요소들을 separator 구분자로 합쳐 `join()` 문자열로 반환

  ```python
  word = '파이썬'
  words = ['너무', '어렵다']
  '.'.join(word)
  >>'파.이.썬'
  '!'.join(words)
  >>'너무!어렵다'
  ```

  

#### 3) 문자 변형

- `.capitalize()`

  - 앞글자를 대문자로 만들어 반환

  ```python
  a = 'hello world, It is ssafy'
  a.capitalize()
  >>'Hello world, it is ssafy'
  ```

- `.title()`

  - ' ' 나 공백 이후를 대문자로 만들어 반환 

  ```python
  a = 'hello world, It is ssafy'
  a.title()
  >>'Hello World, It Is Ssafy'
  ```

- `.upper()`

  - 모두 대문자로 반환

  ```python
  a = 'hello world, It is ssafy'
  a.upper()
  >>'HELLO WORLD, IT IS SSAFY'
  ```

- `.lower()`

  - 모두 소문자로 반환

  ```python
  a = 'Hello World, It is ssafy'
  a.lower()
  >>'hello world, it is ssafy'
  ```

- `.swapcase()`

  - 대 <-> 소문자 변경하여 반환

  ```python
  a = 'Hello World, It is ssafy'
  a.swapcase()
  >>'hELLO wORLD, iT IS SSAFY'
  ```

#### 

#### 4) 기타 문자열 관련 메소드

```python
dir('string') # 을 통해 확인 가능
```



### 2. 리스트(List)

>변경 가능하다 mutable
>
>순서가 있다 ordered
>
>순회 가능한 iterable



#### 1) 값 추가 및 삭제

- `.append(x)`

  - 리스트에 값을 추가. 원본 자체를 조작하므로 return 되지 않는다
  - return 되지 않는 경우 새로운 변수에 넣을 수 없음

  ```python
  fruit = ['grape', 'apple', 'banana']
  fruit.append('orange')
  print(fruit)
  >>['grape', 'apple', 'banana', 'orange']
  
  new_fruit = fruit.append('orange') >> None
  
  fruit.append(['lemon']) 
  >>['grape', 'apple', 'banana', 'orange', ['lemon']]
  ```

- `.extend(iterable)`

  - 리스트에 iterable(list, range, tuple, string) 값을 추가. return 되지 않는다

  ```python
  fruit = ['grape', 'apple', 'banana']
  fruit.extend(['melon', 'strawberry'])
  print(fruit)
  fruit = ['grape', 'apple', 'banana','melon', 'strawberry']
  
  fruit.extend('lemon')
  >>['grape', 'apple', 'banana', 'l', 'e', 'm', 'o', 'n']
  ```

- `.insert(i, x)`

  - 정해진 위치 `i`에 x 를 추가한다

  ```python
  fruit.insert(0, 'start')
  >>['start', 'grape', 'apple', 'banana']
  
  fruit.insert(len(fruit), 'bye') 
  >>['grape', 'apple', 'banana', 'bye']
  # len(fruit) 초과하는 인덱스를 넣어도 마지막에 추가됨
  ```

- `.remove(x)`

  - 리스트에서 x를 삭제한다

  ```python
  numbers = [1, 2, 3, 4, 4]
  numbers.remove(4)
  print(numbers)
  >>[1,2,3,4] # 한 개씩 삭제, 두개 지우고 싶으면 한 번 더 시행
  numbers.remove(5) >> 값이 없다면 오류
  ```

- `.pop(i)`

  - 정해진 위치 `i`에 있는 값을 삭제하며, 해당 값을 반환.
  - i가 지정되지 않을 경우, 마지막 항복을 삭제 후 반환

  ```python
  a = [1, 2, 3, 4]
  print(a.pop(0))
  print(a)
  >>1
  >>[2,3,4]
  ```

- `.clear()`

  - 리스트의 모든 항목을 삭제

  ```python
  numbers = list(range(1,5))
  print(numbers)
  numbers.clear()
  print(numbers)
  >>[1,2,3,4]
  >>[]
  ```

  

#### 2) 탐색 및 정렬

- `.index(x)`

  - x  값을 해당 위치 값을 반환

  ```python
  word = ['a', 'p', 'p', 'l', 'e']
  word.index('l')
  >>3
  ```

- `.count(x)`

  - 원하는 값의 개수

  ```python
  word = ['a', 'p', 'p', 'l', 'e']
  word.count('p')
  >>2
  
  # count 와 remove 를 활용하여 원하는 값을 모두 삭제해보자
  taget_word = 'p'
  for i in range(word.count(taget_word)):
      word.remove(taget_word)
  print(word)
  >>['a', 'l', 'e']
  ```

- `.sort()`

  - 정렬. 내장함수 `sorted()` 와는 달리 원본 list를 변형 시키고 `None` 반환

  ```python
  number = [1, 24, 3, 100]
  a.sort()
  print(a)
  print(a.sort())
  >> [1, 3, 24, 100]
  >> None
  ```

- `.reverse()`

  - 반대로 뒤집는다

  ```python
  alphabet = ['a', 'b', 'c']
  print(alphabet)
  >>['a', 'b', 'c']
  
  alphabet.reverse()
  print(alphabet)
  >>['c', 'b', 'a']
  ```

  

#### 3) 리스트 복사

- 문자열을 복사와 리스트 복사의 차이

```python
a = 3
b = a
>> 현재 b는 a와 같은 값이지만, b +=2 와 같이 변화시킨다해서 a가 영향을 입지 않는다
```

```python
origin_list = [1, 2, 3]
copy_list = origin_list
>> 둘은 같은 값이며 copy_list[0] = 5로 변화시키면 origin 까지 값이 변한다 id가 같음
```

- 왜 그럴까?

  - 데이터는 변경 가능한 mutable 과 변경 불가능한 immutable 로 나뉜다
    - immutable : 단일데이터 - 숫자(number), 글자(String), 참/거짓(Bool)
    - mutable : 컨테이너 - list, dict, set
  - immutable 은 복사해도 별개의 값으로 보지만, mutable은 변경해버린다

- 리스트 복사방법

  - slice 연산자 사용 `[:]`

  ```python
  a = [1, 2, 3]
  b = a[:] # a[i:j] i 이상 j 미만, 아무것도 없을 경우 전체범위
  >> b는 a의 부분집합를 부른 것으로, 별개의 리스트가 된다
  ```

  - `list()` 활용

  ```python
  a = [1, 2, 3]
  b = list(a)
  >> 위와 같다
  ```

- 2차원 배열을 복사

  - 위의 복사법은 얕은 복사로, 리스트 중첩의 경우 내부 리스트는 계속해서 변화됨

  ```python
  import copy
  a = [1, 2, [1, 2]]
  b = copy.deepcopy(a)
  >> a와 별개의 리스트 b가 된다
  >> 원리를 하고 싶다면 python tutor 를 이용하자
  ```



## 데이터 구조에 사용 가능한 Built-in Function

> iterable 타입 - `list`, `dict`, `set`, `str`, `bytes`, `tuple`, `range` - 에 적용 가능

- `map()`
  - 순회 가능한 데이터구조(iterable) 에 function 적용 후 결과 값을 돌려줌
  - map_object 형태로 반환





- `filter()`





- `zip()`



