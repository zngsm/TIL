import sys; sys.stdin = open("input_1931.txt", "r")

N = int(input())
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    a = [s, e, e - s + 1]
    arr.append(a)

print(arr)
time = 2 ** 31 - 1
cnt = 0
for i in range(N-1, -1, -1):
    if arr[i][1] < time:
        cnt += 1
        time = arr[i][0]

print(cnt)