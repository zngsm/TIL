import sys; sys.stdin = open("input_17298.txt", "r")
s = sys.stdin.readline

N = int(s())
arr = list(map(int, s().split()))

for i in range(N):
    for j in range(i+1, N):
        if arr[i] < arr[j]:
            print(arr[j], end=" ")
            break
    else:
        print(-1, end=" ")
print()