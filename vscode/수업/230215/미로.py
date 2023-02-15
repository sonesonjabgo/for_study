def dfs(sr, sc):
    stack = [(sr, sc)]
    visited = [[0] * N for _ in range(N)]

    visited[sr][sc] = 1
    while stack:
        # 현재 위치
        cr, cc = stack[-1]
        if arr[cr][cc] == 2:
            return 1
        # top에서 이동할 수 있는 모든 경로 살펴보기
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]: # 상 하 좌 우 순으로
            nr = cr+dr
            nc = cc+dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] and not visited[nr][nc]: # 갈 수 있음
                stack.append((nr,nc))
                # 방문했음을 표시
                visited[nr][nc] = 1
                break

        else:
            stack.pop()
    return 0

arr = [
    [1,1,1,0,0],
    [0,0,1,1,1],
    [0,0,1,0,0],
    [0,0,1,1,1],
    [2,1,1,0,0]
]

N = 5

print(dfs(0,0))