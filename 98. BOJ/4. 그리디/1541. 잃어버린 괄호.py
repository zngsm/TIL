import sys; sys.stdin = open("input_1541.txt", "r")
s = sys.stdin.readline

figures = s()

total = 0
number = ''
isplus = True
for i in range(len(figures)):
    if figures[i].isdigit():
        number = number + figures[i]
    else:
        if isplus:
            total += int(number)
        else:
            total -= int(number)
        if figures[i] == '-':
            isplus = False
        number = ''
else:
    if isplus:
        total += int(number)
    else:
        total -= int(number)

print(total)