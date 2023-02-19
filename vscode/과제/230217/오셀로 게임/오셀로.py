import sys
sys.stdin = open("sample_input(1).txt", "r")

# arr[i][j]의 4방향 검사가 필요함 땡~ 대각선도 해야돼
# 상 우 하 좌
lr = [-1, 0, 1, 0]
lc = [0, -1, 0, 1]


def rock():
    for i in range(N):
        for j in range(N):
            if 0 <= i-1 < N and 0 <= j-1 < N and 0 <= i+1 < N and 0 <= j+1 < N:
                for k in range(2):
                    if arr[i+lr[k]][j+lc[k]] == arr[i+lr[k+2]][j+lc[k+2]]:
                        if arr[i+lr[k]][j+lc[k]] == 1:
                            arr[i][j] = 1
                        elif arr[i+lr[k]][j+lc[k]] == 2:
                            arr[i][j] = 2


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    if N == 4:
        arr[1][1] = 2
        arr[2][2] = 2
        arr[1][2] = 1
        arr[2][1] = 1
    elif N == 6:
        arr[2][2] = 2
        arr[3][3] = 2
        arr[2][3] = 1
        arr[3][2] = 1
    elif N == 8:
        arr[3][3] = 2
        arr[4][4] = 2
        arr[3][4] = 1
        arr[4][3] = 1

    for _ in range(M):
        r, c, s = map(int, input().split())
        # print(r, c, s)
        arr[c-1][r-1] = s
    rock()
    print(arr)