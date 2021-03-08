import sys; sys.stdin = open("input_10773.txt", "r")
s = sys.stdin.readline

N = int(s())

arr = []
for i in range(N):
    num = int(s())
    if num == 0:
        arr.pop()
    else:
        arr.append(num)

print(sum(arr))