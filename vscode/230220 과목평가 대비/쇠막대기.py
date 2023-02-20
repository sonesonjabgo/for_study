T = int(input())

for tc in range(1, T+1):
    data = input()
    stack = []
    stick = 0
    for i in range(len(data)):
        if data[i] == '(':
            stack.append(data[i])

        else:
            if data[i-1] == '(':
                stack.pop()
                stick += len(stack)
            else:
                stack.pop()
                stick += 1

    print(f'#{tc} {stick}')