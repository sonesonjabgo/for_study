# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = input()
    stack = []
    count = 0
    i = 0
    while i < len(data):
        if data[i] == '(':
            stack.append(data[i])
            if data[i+1] == ')':
                stack.pop()
                i += 1
                if stack:
                    count += len(stack)
            i += 1
        else:
            i += 1
            stack.pop()
            count += 1
    print(f'#{test_case} {count}')




