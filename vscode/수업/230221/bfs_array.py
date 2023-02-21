# bfs로 행렬 탐색
arr = [
[0,0,1,0,0],
[0,1,1,1,1],
[0,0,1,1,0],
[0,0,0,1,0],
[0,0,0,0,0]
]
N = 5
# arr안의 1의 개수를 찾아라
# 상하좌우로 연결된 1의 개수 찾기

queue = [] # 리스트지만 맨 뒤에 넣고 앞에서 빼는 식으로 활용
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            queue.append((i,j))
            visited[i][j] = 1

            cnt = 0
            while queue:
                ci, cj = queue.pop(0)
                cnt += 1
                for di,dj in ([(-1,0),(1,0),(0,-1),(0,1)]):
                    ni,nj = ci+di, cj+dj
                    # 정상 범위 안에 있으면서,
                    if 0 <= ni < N and 0 <= nj < N:
                        # 1이고, 방문하지 않았으면, 방문할 노드에 추가
                        if arr[ni][nj] and not visited[ni][nj]:
                            queue.append((ni,nj))
                            visited[ni][nj] = 1
            print(cnt)