import sys
sys.stdin = open("input.txt", "r")

def zegob(n, x): # 제곱시킬 수와 얼만큼 제곱시킬 지
    if x == 0:
        return 1
    else:
        return n * zegob(n, x-1)

T = 10
for test_case in range(1, T + 1):
    tc = input()
    a, b = map(int, input().split())
    result = zegob(a, b)
    print(f'#{tc} {result}')