# python 07_21



## 반복제어(`break`, `continue`, `for-else`)

### 1. break

> 반복문을 종료한다.

- for 나 while 문에서 탈출

> break가 걸리면 이후 어떤 것도 시행되지 않는다

```python
# while문 사용
n = 0
while True:
  if n >= 3:
    print('브레이크 걸리는 시점', n)
    break
  print(n) # break 걸리면 시행되지 않음
  n += 1 # break 걸리면 시행되지 않음
print('반복문 탈출!')
```

```python
# for문 사용
for i in range(10):
  if i > 1:
    print('break할거야')
    break
  print(i)
```

```python
# 활용 예시
rice = ['보리', '보리', '보리', '쌀', '보리']

# 아래에 코드를 작성하세요.
for i in rice:
  print(i)
  if i == '쌀':
   print('잡았다!')
   break # break 없으면 이후 보리까지 계속 출력됨
```





### 2. continue

>  continue 이후의 코드는 수행하지 않고, 다음 요소부터 계속하여 반복 수행

```python

```





### 3. for-else

> 끝까지 반복문을 시행한 이후에 실행된다.

- for의 경우, 조건이 거짓이 되고, while의 경우 종료할 때 실행된다

```python

```





### 4. pass

> 아무것도 하지 않는다.

- 문법적으로 문장이 필요하지만, 프로그램이 특별히 할 일이 없을 때 자리를 채우는 용도로 사용할 수 있다.

```python

```

