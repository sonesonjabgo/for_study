import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    p = input()
    t = input()
    M = len(p)
    N = len(t)

    # N과 M의 시작 인덱스
    i = 0
    j = 0
    # 시작 인덱스의 값이 같지 않으면 i에 1을 더할 것임
    while j < M and i < N:
    # 이 조건을 충족 못하면 비교해야 할 인덱스가 p와 t의 길이를 넘어간 것임
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    # 위의 두 줄은 반복문에서 항상 작용된다.
    # if 문의 조건이 맞을 경우에는 처음 비교했던 인덱스 다음 것을 비교 할 것이고
    # 비교하던 중 틀렸을 경우 i - j를 하면 맞게돼서 이동한 인덱스를 빼는 것이다.
    # 그리고 j는 -1로 선언하는 이유는 아래에서 올 코드에서 1을 더해 0으로 초기화 시켜주는 것
    if j == M:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')

