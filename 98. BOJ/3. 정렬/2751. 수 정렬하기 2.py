import sys

s = sys.stdin.readline

N = int(s())
arr = list(int(s()) for _ in range(N))
ans = sorted(arr)
print(*ans, sep='\n')