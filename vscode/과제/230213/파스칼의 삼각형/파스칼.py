# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    print(f'#{test_case}')
    for i in range(N):
        pascal = ['1'] + [str(i)] * i
        if i >= 2:
            pascal[-1] = '1'
        print(' '.join(pascal))