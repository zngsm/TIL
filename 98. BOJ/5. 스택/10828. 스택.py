import sys; sys.stdin = open("input_10828.txt", "r")
s = sys.stdin.readline

N = int(s())

stack = []
for _ in range(N):
    command = s().split('\n')[0]
    if command == 'size':
        print(len(stack))
        continue
    elif command.split()[0] == 'push':
        stack.append(command.split()[1])
        continue
    if not stack:
        if command == 'pop' or command == 'top':
            print(-1)
        elif command == 'empty':
            print(1)
    else:
        if command == 'pop':
            print(stack.pop())
        elif command == 'empty':
            ans = 0
            print(0)
        elif command == 'top':
            print(stack[-1])