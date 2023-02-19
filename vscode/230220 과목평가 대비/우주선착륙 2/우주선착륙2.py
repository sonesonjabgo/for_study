import sys
sys.stdin = open("input2.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행렬 전부 8방향 검사해야 됨
    # 좌 좌상 상 우상 우 우하 하 좌하
    lr = [0, -1, -1, -1, 0, 1, 1, 1]
    ls = [-1, -1, 0, 1, 1, 1, 0, -1]
    result = 0

    for i in range(N):
        for j in range(M):
            count = 0
            for k in range(8): # 8방향 검사를 위한 k
                # 검사를 하기 전에 인덱스 범위 넘는 경우를 제외해줌
                if 0 <= i+lr[k] < N and 0 <= j+ls[k] < M:
                    if arr[i][j] > arr[i+lr[k]][j+ls[k]]:
                        count += 1
            if count >= 4:
                result += 1
    print(f'#{tc} {result}')