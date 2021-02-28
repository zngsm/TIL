import sys
s = sys.stdin.readline

N = int(s())
cnt = [0 for _ in range(10001)]
for _ in range(N):
    cnt[int(s())] += 1

for i in range(10001):
    for j in range(cnt[i]):
        print(i)
