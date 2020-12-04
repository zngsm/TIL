def operate(num):
    return num % c
a, b, c = map(int, input().split())
ans = [operate(a + b), operate(operate(a) + operate(b)), operate((a * b)), operate(operate(a) * operate(b))]
for i in ans:
    print(i)