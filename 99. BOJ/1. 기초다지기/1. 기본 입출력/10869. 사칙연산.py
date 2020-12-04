n, m = map(int, input().split())
ans = [n + m, n - m, n * m, n // m, n % m]
for A in ans:
    print(A)