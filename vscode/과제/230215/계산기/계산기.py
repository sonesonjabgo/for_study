import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    data = input()
    stack = []
    numbers = []

    for i in range(N):
        if data[i] in '0123456789':
            numbers.append(data[i])
        else:
            if not stack:
                stack.append(data[i])
            else:
                numbers.append(stack.pop())
                stack.append(data[i])

    if stack:
        numbers.append(stack.pop())

    numbers = ''.join(numbers)

    for num in numbers:
        if num in '0123456789':
            stack.append(int(num))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            sumn = op1 + op2
            stack.append(sumn)

    print(f'#{test_case} {stack[-1]}')
