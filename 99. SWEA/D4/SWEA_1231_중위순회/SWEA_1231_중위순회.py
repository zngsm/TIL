import sys; sys.stdin = open("input_1231.txt")

for tc in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(N)]
    for _ in range(N):
        l = list(map(int, input().split()))
        if