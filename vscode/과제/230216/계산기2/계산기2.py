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

#########################################
# 1. 후위 표기식으로 바꾸기
# 1-1. 토큰을 읽으면서 숫자라면 출력, 연산자라면 stack에 저장
# 1-2. 단, 우선순위가 높은 연산자가 먼저나와야 하니까 위에 있어야 합니다.
#      그래서 우선순위가 낮은 연산자라면, 우선순위 높은 연산자를 빼고 스택에 푸쉬
T = 10
for tc in range(1, T+1):
    N = int(input())
    data = input()
    # 후위 표기식으로 바꾸고
    postfix = ''
    stack = []
    for i in range(N):
        if data[i] in '0123456789':
            postfix += data[i]
        # 연산자
        # 곱하기라면 stack에 push
        # 더하기라면 다 빼고 넣기
        else:
            if data[i] == '*':
                if not stack:
                    stack.append(data[i])
                else:
                    if stack[-1] == '+':
                        stack.append(data[i])
                    else:
                        postfix += stack.pop()
                        stack.append(data[i])
            else:
                # 비어있으면 그냥 넣기
                if not stack:
                    stack.append(data[i])
                # 아니라면, 다 빼고 넣기
                else:
                    while stack:
                        postfix += stack.pop()
                    stack.append(data[i])
    while stack:
        postfix += stack.pop()

    print(postfix)
    # 연산하기
    # 연산자가 나오면 피연산자 2개 빼서 연산해서 다시 스택에 넣기
    # 피연산자는 스택에 넣기
    stack = []
    for i in range(N):
        if postfix[i] in '0123456789':
            # 연산 해야되니 숫자로 바꿔서 넣어주기
            stack.append(int(postfix[i]))
        else:
            n1 = stack.pop()
            n2 = stack.pop()
            if postfix[i] == '*':
                stack.append(n1*n2)
            else:
                stack.append(n1+n2)