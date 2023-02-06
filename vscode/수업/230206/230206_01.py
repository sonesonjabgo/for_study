# 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
# 오른쪽부터 시계방향으로 우, 하, 좌, 상 
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 3

for i in range(N):
    for j in range(N):
        for k in range(4): # 기준칸의 주변의 4가지 방향으로 탐색
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N: 
            # 배열 밖의 부분을 가리키는 것을 제외시킴
                print(i, j, ni, nj)