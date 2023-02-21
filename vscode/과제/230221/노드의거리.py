def bfs(v, N):
    visited = [0] * (N + 1)
    q = [v]
    visited[v] = 1

    while q:
        front = q.pop(0)  # 디큐
        # 현재 노드에서 방문할 수 있는 경로 탐색하기
        for node in adjL[front]:
            # 노드에 방문하지 않았다면 방문목록에 저장
            if visited[node] == 0:
                # node 인큐
                q.append(node)
                # node 인큐되었음 표시
                visited[node] = visited[front] + 1
    return visited
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]
    adjL = [[] for _ in range(V+1)]
    for nod in data:
        adjL[nod[0]].append(nod[1])
        adjL[nod[1]].append(nod[0])
    # print(adjL)
    ts, te = map(int, input().split())
    # print(bfs(1, V))
    if bfs(ts, V)[te] <= 1:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {bfs(ts, V)[te] - 1}')