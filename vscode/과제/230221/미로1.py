def bfs(start):
    r, c = start
    queue = [start]
    visited = [[0] * 16 for _ in range(16)]
    visited[r][c] = 1

    while queue:
        r,c = queue.pop(0)
        # 상 우 하 좌
        for di, dj in [(-1,0),(0,1),(1,0),(0,-1)]:
            ni = r+di
            nj = c+dj
            if 0 <= ni < 16 and 0 <= nj < 16:
                if arr[ni][nj] != 1 and visited[ni][nj] == 0:
                    queue.append((ni,nj))
                    visited[ni][nj] = 1
    return visited





for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, list(input()))) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                start = (i,j)
            elif arr[i][j] == 3:
                ei, ej = i,j

    result = bfs(start)
    print(f'#{tc} {result[ei][ej]}')