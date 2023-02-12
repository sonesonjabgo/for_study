for test_case in range(1, 11):
    M = int(input())
    letters = [input() for _ in range(8)]
    ##### 가로 ######
    count = 0
    for i in range(8):
        k = 0  # 비교 시작 위치
        j = 0  # 비교할 문자 인덱스
        while k < 8 - M + 1:
            if letters[i][j + k] == letters[i][M - 1 + k - j]:
                j += 1  # 맞을 경우 다음 글자 비교해야 함
                if j == (M // 2):
                    count += 1
                    k += 1
                    j = 0
            else:

                j = 0  # 몇 글자 맞다가 틀릴 경우 초기화해야 함
                k += 1  # 글자가 틀릴 경우 비교 시작하는 위치를 하나 옮김


        ##### 세로 ######
    for i in range(8):
        k = 0  # 비교 시작 위치
        j = 0  # 비교할 문자 인덱스
        result = ''
        while k < 8 - M + 1:
            if letters[j + k][i] == letters[M - 1 + k - j][i]:
                # result += letters[i][j+k]
                j += 1  # 맞을 경우 다음 글자 비교해야 함
                if j == (M // 2):
                    count += 1
                    k += 1
                    j = 0
            else:

                j = 0  # 몇 글자 맞다가 틀릴 경우 초기화해야 함
                k += 1  # 글자가 틀릴 경우 비교 시작하는 위치를 하나 옮김
    print(f'#{test_case} {count}')