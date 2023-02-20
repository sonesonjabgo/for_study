import sys
sys.stdin = open("in1.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가운데를 구할 필요 없음
    # M 스프레이의 세기에 따라
    # 검사할 범위를 다르게 만들어서
    # 인덱스의 합 구하면 됨
    # 기준점을 두고 십자가 방향의 인덱스 값의 합
    # X 방향의 인덱스 값
    # 범위를 넘어가는 경우 제외해야 함
    crossfly = 0
    for i in range(N):
        for j in range(N):
            fly = arr[i][j]
            for k in range(1, M):
                if i + k < N:
                    fly += arr[i + k][j]
                if 0 <= i - k:
                    fly += arr[i - k][j]
                if j+k < N:
                    fly += arr[i][j+k]
                if 0 <= j-k:
                    fly += arr[i][j-k]
            if fly > crossfly:
                crossfly = fly

    Xfly = 0
    for i in range(N):
        for j in range(N):
            fly = arr[i][j]
            for k in range(1, M):
                if 0 <= i-k and 0 <= j-k:
                    fly += arr[i-k][j-k]
                if i+k < N and 0 <= j-k:
                    fly += arr[i+k][j-k]
                if i+k < N and j+k < N:
                    fly += arr[i+k][j+k]
                if 0 <= i-k and j+k < N:
                    fly += arr[i-k][j+k]
            if fly > Xfly:
                Xfly = fly

    if crossfly > Xfly:
        print(f'#{tc} {crossfly}')
    else:
        print(f'#{tc} {Xfly}')