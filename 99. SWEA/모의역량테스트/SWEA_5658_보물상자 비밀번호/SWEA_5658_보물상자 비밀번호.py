import sys; sys.stdin = open("input.txt", "r")
from collections import deque
for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    password = list(input())
    l = N// 4
    number = []
    for _ in range(l):
        last = password[-1]
        for i in range(N - 1, 0, -1):
            password[i] = password[i-1]
        password[0] = last
        for j in range(0, N, l):
            if password[j:j+l] not in number:
                number.append(password[j:j+l])
    Alphabet = ['A','B','C','D','E','F']
    real_num = []
    for i in range(len(number)):
        m = len(number[i])
        total = 0
        for j in range(m-1, -1, -1):
            if number[i][j].isdigit():
                total += int(number[i][j]) * (16 ** (m-1-j))
            else:
                total += (10 + Alphabet.index(number[i][j])) * (16 ** (m-1-j))
        real_num.append(total)

    real_num.sort(reverse=True)

    print('#{} {}'.format(tc, real_num[K -1 ]))