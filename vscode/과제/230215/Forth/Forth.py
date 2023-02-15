# # 후위 표기법으로 된 것 계산하는 문제
#
# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    texts = input().split()
    stack = []
    operator = ['+','-','*','/','.']
    result = 'error'
    for text in texts:
        if text == '.':
            if len(stack) > 1:
                result = 'error'
            else:
                result = stack[-1]
            break
        if text not in operator:
            stack.append(int(text))
        else:
            if len(stack) < 2:
                result = 'error'
                break
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if text == '+':
                    num = op1 + op2
                    stack.append(num)
                elif text == '-':
                    num = op1 - op2
                    stack.append(num)
                elif text == '*':
                    num = op1 * op2
                    stack.append(num)
                elif text == '/':
                    num = op1 / op2
                    stack.append(num)


    print(f'#{test_case} {result}')

