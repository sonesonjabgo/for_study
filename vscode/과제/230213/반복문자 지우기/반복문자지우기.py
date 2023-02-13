import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    stack = []
    data = input()
    for i in data:
        if stack and i == stack[-1]:
        # stack이 빈 리스트가 아니고 i가 stack의 마지막이 같을 때
        # stack이 빈 리스트가 아닌 조건을 넣지 않으면
        # 두 번째 조건에서 인덱스 에러가 나옴
            stack.pop()
        else:
            stack.append(i)
    print(f'#{test_case} {len(stack)}')






