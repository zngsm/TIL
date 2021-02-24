import sys; sys.stdin = open('input_11047.txt', 'r')

N, K = map(int, input().split())
coin = list(int(input()) for _ in range(N))
cnt = 0
k = K
i = N - 1
while k > 0:
    if k == 0:
        break
    if coin[i] > k:
        i -= 1
    else:
        n = k // coin[i]
        k -= coin[i] * n
        cnt += n
print(cnt)