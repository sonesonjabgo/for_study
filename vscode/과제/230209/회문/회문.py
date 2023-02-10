import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    M = lst[1]
    letters = [input() for _ in range(N)]
    for i in range(N):
        k = 0  # 비교 시작 위치
        j = 0  # 비교할 문자 인덱스
        result = ''

        while k < N - M + 1:
            if letters[i][j + k] == letters[i][M - 1 + k - j]:
                # result += letters[i][j+k]
                j += 1  # 맞을 경우 다음 글자 비교해야 함
                if j == (M // 2):
                    for a in range(k, k + M):
                        result += letters[i][a]
                    break
            else:
                result = ''  # 틀렸으니까 초기화
                j = 0  # 몇 글자 맞다가 틀릴 경우 초기화해야 함
                k += 1  # 글자가 틀릴 경우 비교 시작하는 위치를 하나 옮김
        if result:
            break
    print(f'#{test_case} {result}')