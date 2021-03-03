import sys; sys.stdin = open("input_11650.txt", "r")

s = sys.stdin.readline

N = int(s())
arr = [tuple(map(int, s().split())) for _ in range(N)]

for x, y in sorted(arr):
    print(x, y)