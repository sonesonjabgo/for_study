def bfs(start, end):
    queue = []
    # 상 좌 하 우
    lr = [-1, 0, 1, 0]
    lc = [0, -1, 0, 1]
    queue.append(start)
    r, c = start
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    # 여기다가 start부터 어떤 자리까지 도달하는데 움직여야 하는 거리를 기록할 것
    # 방문했었다 와 가는데까지 얼마나 걸렸다의 기능을 하게 됨.
    while queue: # end를 만날때 끝내고 visited를 가져와서 visited[end] 인덱스 값을 확인해야 함.
        si, sj = queue.pop(0)
        for i in range(4):
            if 0 <= si+lr[i] < N and 0 <= sj+lc[i] < N:
                if arr[si+lr[i]][sj+lc[i]] == 0 and visited[si+lr[i]][sj+lc[i]] == 0:
                    queue.append((si+lr[i], sj+lc[i]))
                    visited[si + lr[i]][sj + lc[i]] = visited[si][sj] + 1

    ei, ej = end
    results = []
    for k in range(4):
        if 0 <= ei+lr[k] < N and 0 <= ej+lc[k] < N:
            if arr[ei+lr[k]][ej+lc[k]] == 0:
                results.append(visited[ei+lr[k]][ej+lc[k]])
    else:
        if not results:
            results.append(0)
    result = min(results)
    return result
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = (i,j)
            elif arr[i][j] == 3:
                end = (i,j)
    result = bfs(start, end)
    if result <= 1:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {bfs(start, end)-1}')
