import sys; sys.stdin = open("input_11650.txt", "r")

s = sys.stdin.readline

N = int(s())
arr = [tuple(map(int, s().split())) for _ in range(N)]

ans = sorted(arr, key = lambda x : (x[1], x[0]))
for x, y in ans:
    print(x, y)
