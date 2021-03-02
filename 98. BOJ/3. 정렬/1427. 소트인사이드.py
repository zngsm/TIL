import sys
s = sys.stdin.readline
N = int(s())
value = []
n = N
while n > 0:
    v = n % 10
    value.append(v)
    n //= 10

value = sorted(value, reverse=True)
total = 0
for i in range(len(value)):
    total += (value[i] * (10 ** (len(value) - i - 1)))
print(total)