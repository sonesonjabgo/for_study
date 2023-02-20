import sys
sys.stdin = open("input2.txt", "r")

# 받은 배열을 전부 8방향 탐색함
# 그 중 해당 인덱스 값보다 인덱스 값이 작은 곳이 4곳 이상이라면
# 카운트 증가

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 높이 M은 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 기준점을 두고 8방향 상하좌우 상좌 상우 하좌 하우
    # 좌 상좌 상 상우 우 하우 하 하좌
    lr = [0, -1, -1, -1, 0, 1, 1, 1]
    lc = [-1, -1, 0, 1, 1, 1, 0, -1]
    result = 0

    for i in range(N):
        for j in range(M):
            count = 0
            for k in range(8):
                if 0 <= i+lr[k] < N and 0 <= j+lc[k] < M:
                    if arr[i][j] > arr[i+lr[k]][j+lc[k]]:
                        count += 1
            if count >= 4:
                result += 1
                # 해당 인덱스가 범위를 넘어가는 경우를 제외해줘야 함.
                # 해당 인덱스가 값이 큰 경우 카운트하고 값이 4보다 크면
                # result의 값 상승
    print(f'#{tc} {result}')