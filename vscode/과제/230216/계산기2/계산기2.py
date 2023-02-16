import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    data = input()

    stack = []
    pr = ''
    operator = {'+':1, '*':2}

    for i in range(N):
        if data[i] in '0123456789':
            pr += data[i]

        else:
            if not stack:
                stack.append(data[i])
            else:
                while stack and operator[data[i]] <= operator[stack[-1]]:
                    pr += stack.pop()
                stack.append(data[i])
    while stack:
        pr += stack.pop()
    # print(stack)

    stack = []
    for num in pr:
        if num in '0123456789':
            stack.append(int(num))
        else:
            if num == '+':
                op2 = stack.pop()
                op1 = stack.pop()
                sumn = op1 + op2
                stack.append(sumn)
            elif num == '*':
                op2 = stack.pop()
                op1 = stack.pop()
                sumn = op1 * op2
                stack.append(sumn)

    print(f'#{tc} {stack[-1]}')
