import sys; sys.stdin = open("input_4949.txt", "r")
s = sys.stdin.readline

while True:
    phar = s().rstrip()
    if phar == '.':
        break
    stack = []
    for i in phar:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack:
                left = stack.pop()
                if left == '[':
                    ans = 'no'
                    break
            else:
                ans = 'no'
                break
        elif i == ']':
            if stack:
                left = stack.pop()
                if left == '(':
                    ans = 'no'
                    break
            else:
                ans = 'no'
                break
    else:
        if stack:
            ans = 'no'
        else:
            ans = 'yes'
    print(ans)
