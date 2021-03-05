import sys; sys.stdin = open("input_1931.txt", "r")
s = sys.stdin.readline
N = int(s())
arr = [tuple(map(int, s().split())) for _ in range(N)]
arr = sorted(arr, key = lambda x : (x[1], x[0]))
i = 0
start = -1
ans = []
while True:
    if not arr:
        break
    if start == 2 ** 31 - 1:
        break
    A = arr.pop(0)
    if A[0] >= start:
        ans.append(A)
        start = A[1]
print(len(ans))
