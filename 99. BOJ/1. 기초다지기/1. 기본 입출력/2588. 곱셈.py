n = int(input())
m = int(input())
t = m
while t > 0:
    tm = t % 10
    print(n * tm)
    t //= 10
print(n * m)