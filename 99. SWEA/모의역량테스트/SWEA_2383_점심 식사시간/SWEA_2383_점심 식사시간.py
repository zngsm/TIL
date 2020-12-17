# import sys; sys.stdin = open("input.txt", "r")
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     step = []
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] > 1:
#                 step.append((arr[i][j], i, j)) # 계단 높이, y, x 순
#     num = 1
#     if_go_A, if_go_B = [], []
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 1:
#                 goA = step[0][0] + abs(i - step[0][1]) + abs(j - step[0][2])
#                 goB = step[1][0] + abs(i - step[1][1]) + abs(j - step[1][2])
#                 if_go_A.append([num, goA + 1, goA-goB, step[0][0]])
#                 if_go_B.append([num, goB + 1, goB-goA, step[1][0]])
#                 num += 1
#     if_go_A = sorted(if_go_A, key=lambda x: x[1])
#     if_go_B = sorted(if_go_B, key=lambda x: x[1])
#     A, B = 0, 0
#     a_list, b_list = [], []
#     idx = 0
#
#
#     print('#{} {} & {}'.format(tc, if_go_A, if_go_B))
#

# def solve(w):
#     arr = []
#     for i in range(len(w)):
#         arr.append(w[i])
#     for i in range(len(w) - 1, -1, -1):
#         arr.append(w[i])
#     return arr
# word = input()
# print(solve(word))


# 1~6까지 숫자가 n개씩 있을 때, n개의 숫자를 뽑는 중복 순열?
# N = int(input())
# from itertools import product
# for i in product(range(1, 7), range(1, 7)):
#     print(i, end=" ")
def abc():
    a = 10
a = 1
a = 2
a = 3
abc()
a = 4
a = 5
a = 6
a = 7
a = 8

