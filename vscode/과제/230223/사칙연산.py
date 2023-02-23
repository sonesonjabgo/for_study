def order(T):
    if T == 0:
        return
    order(tree[1][T])
    order(tree[2][T])
    rst_list.append(tree[0][T])


for tc in range(1, 11):
    N = int(input())
    tree = [[0] * (N+1) for _ in range(3)]

    data = [input().split() for _ in range(N)]
    for i in data:
        if len(i) == 4:
            tree[0][int(i[0])] = i[1]
            tree[1][int(i[0])] = int(i[2])
            tree[2][int(i[0])] = int(i[3])
        else:
            tree[0][int(i[0])] = int(i[1])

    rst_list = []
    order(1)
    oper = ['+', '-', '*', '/']
    stack = []

    for k in rst_list:
        if k not in oper:
            stack.append(k)
        else:
            if len(stack) >= 2:
                if k == '+':
                    op2 = stack.pop()
                    op1 = stack.pop()
                    stack.append(op1 + op2)
                elif k == '-':
                    op2 = stack.pop()
                    op1 = stack.pop()
                    stack.append(op1 - op2)
                elif k == '*':
                    op2 = stack.pop()
                    op1 = stack.pop()
                    stack.append(op1 * op2)
                if k == '/':
                    op2 = stack.pop()
                    op1 = stack.pop()
                    stack.append(op1 / op2)

    result = stack[-1]
    print(f'#{tc} {result:.0f}')