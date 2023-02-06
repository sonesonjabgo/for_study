# 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
N = 3
for i in range(N):
    for j in range(N):
        for di, dj in [[0,1] [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                print(i, j, ni, nj)