import sys; sys.stdin = open("input_11399.txt", "r")
s = sys.stdin.readline
N = int(s())
arr = list(map(int, s().split()))
arr = sorted(arr)

total = wait = 0
for i in range(N):
    total += (wait + arr[i])
    wait += arr[i]
print(total)