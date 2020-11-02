## 데이터구조 2

> 순서가 없는 데이터  : 세트(set), 딕셔너리(dictionary)



### 세트(set)

> 변경가능하다 mutable
>
> 순서가 없다 unordered
>
> 순회 가능하다 iterable



#### 1) 추가 및 삭제

- `.add(elem)`

  -  elem 을 세트에 추가

  ```python
  fruit = {'사과', '바나나', '수박'}
  fruit.add('포도')
  print(fruit)
  >>{'사과', '바나나', '수박', '포도'}
  ```

- `.update(*others)` *others => 가변인자가 몇개가 들어오든 받아준다는 의미.

  - 여러가지 값을 추가. 반드시 iterable 구조여야한다

  ```python
  fruit = {'사과', '바나나', '수박'}
  fruit.update({'포도', '레몬'},range(1,3),{'토마토', '딸기'})
  print(fruit)
  >>{'딸기', 1, 2, '수박', '레몬', '사과', '바나나', '포도', '토마토'}
  ```

- `. remove(elem)`

  -  elem을 세트에서 삭제. 해당 사항이 없을 경우 KeyError.

  ``` python
  a = {1, 2, 3}
  a.remove(1)
  >>{2, 3}
  a.remove(5)
  >>KeyError
  ```

- `.discard(elem)`

  - elem을 세트에서 삭제. 해당 사항이 없어도 에러 발생하지 않는다

  ```python
  a = {1, 2, 3}
  a.discard(1)
  >>{2, 3}
  a.discard(5)
  >>{1, 2, 3}
  ```

- `.pop()`

  - 임의의 원소를 제거 후 반환

  ```python
  a = {1, 2, 3}
  result = a.pop()
  print(a.pop())
  print(result)
  >>1
  >>{2, 3}
  ```

  

### 딕셔너리

> 변경하능하다 mutable
>
> 순서가 없다 unordered
>
> 순회가능하다 iterable



#### 1) 조회



- `.get(key[,default])`

  - key를 통해 value 를 가져옴
  - 없으면 default, default 는 None. KeyError는 발생하지 않는다

  ```python
  numbers = {'n1' : 1, 'n2' : 2, 'n3' :3}
  print(numbers.get('n1'))
  print(numbers.get('n4'))
  print(numbers.get('n4', 0))
  print(numbers.get('n1', 0))
  >>1
  >>None
  >>0
  >>1
  ```

  

#### 2) 추가 및 삭제

- `.pop(key[, default])`

  - key 가 딕셔너리내에 있을 경우, 제거 후 해당 값을 돌려줌. 
  - 없으면 default, default 가 지정되어있지않는 상태에서 발생하면 KeyError

  ```python
  numbers = {'n1' : 1, 'n2' : 2, 'n3' :3}
  result = numbers.pop('n1'
  print(numbers.pop('n1'))
  print(result)
  >>{'n2' : 2, 'n3' :3}
  >>1
  ```

- `.update()`

  - 제공하는 key, value로 덮어씀

  ```python
  numbers = {'n1' : 1, 'n2' : 2, 'n3' :3}
  numbers.update('n1' : 'no.1')
  print(numbers)
  >>{'n1' : 'no.1', 'n2' : 2, 'n3' :3}
  ```

  

#### 3) 딕셔너리 순회

- `dict[key] = value`

- `for` 를 활용해 dictionary 순회

  - `key` 활용

  ```python
  for key in dict:
      print(key)
      print(dict[key])
  >> key 값 순서대로 출력, value 순서대로 출력
  ```

  - `.keys()` 활용

  ```python
  for key in dict.keys():
      print(key)
      print(dict[key])
  >> key 값 순서대로 출력, value 순서대로 출력
  ```

  - `.values()` 활용

  ```python
  for val in dict.values():
      print(val)
  >> value 순서대로 출력
  ```

  - `.items()` 활용

  ```python
  for key, val in dict.items():
      pring(key, val)
  >> (key, value) 순서대로 출력 
  ```