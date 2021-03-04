import sys; sys.stdin = open("input_10814.txt", "r")
#

s = sys.stdin.readline
N = int(s())
arr = [list(s().split()) + [i] for i in range(N)]

arr = sorted(arr, key= lambda  x: (int(x[0]), x[2]))
# arr = sorted(arr, key= lambda x : (x[1], x[0]))
for i in arr:
    print(i[0], i[1])
# t = int(sys.stdin.readline())
#
# str_ = []
#
# count = 0
# for i in range(t):
#     count += 1
#     b, c = map(str, sys.stdin.readline().split())
#     str_.append([b, c, count])
#
# str_.sort(key=lambda x: (x[0], x[2]))
#
# for i in range(len(str_)):
#     print(str_[i][0], str_[i][1])
# # s = sys.stdin.readline
# # N = int(s())
# # # arr = [list(s().split()) + [i] for i in range(N)]
# # mem = {}
# #
# # for _ in range(N):
# #     age, name = map(str, s().split())
# #     # print(age, name)
# #     if mem.get(age):
# #         mem[age] += [name]
# #     else:
# #         mem[age] = [name]
# #
# # for key in sorted(mem.keys()):
# #     for j in mem[key]:
# #         print(key, j)
# # arr = sorted(arr, key= lambda  x: (x[0], x[2]))
# # # arr = sorted(arr, key= lambda x : (x[1], x[0]))
# # for i in arr:
# #     print(i[0], i[1])
#
