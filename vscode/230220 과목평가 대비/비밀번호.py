# import sys
# sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    N, password = input().split()
    N = int(N)
    stack = []
    for i in range(N):
        if stack and stack[-1] == password[i]:
            stack.pop()
        elif not stack or stack[-1] != password[i]:
            stack.append(password[i])
    stack = ''.join(stack)
    print(f'#{test_case} {stack}')

# 스택에 password를 순차적으로 옮긴다
# 단, 스택의 마지막 숫자가 들어올 숫자와 같다면
# 스택의 마지막 숫자를 지우고 들어올 숫자를 건너뛴다.