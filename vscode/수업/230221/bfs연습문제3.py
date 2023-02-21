# 7 8  노드의 수 / 연결 노드 수 (간선)
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

def bfs(v, N): # v: 시작노드, N: 마지막 노드
# bfs는 현재 위치에서 방문할 수 있는 모든 경로를 일단 저장
# 저장한 순서대로 방문하기

    # visited 생성
    visited = [0] * (N+1)
    # Queue 생성
    # 시작점 enqueue
    q = [v]
    # 시작점 visited에 표시
    visited[v] = 1
    
    while q: # 큐가 비어있지 않으면
        # dfs와는 다르게 다시 돌아올 일이 없어서 빼고 시작
        front = q.pop(0) # 디큐
        
        print(front, end=' ')  # t에서 처리할 일
        # t에 인접이고 방문한 적 없는 v

        # 현재 노드에서 방문할 수 있는 경로 탐색하기
        for node in adjL[front]:
            # 노드에 방문하지 않았다면 방문목록에 저장
            if visited[node] == 0:
                # node 인큐
                q.append(node)
                # node 인큐되었음 표시
                visited[node] = visited[front] + 1
V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjL = [[] for _ in range(V+1)] # 0번은 안쓰고 1번부터 V번까지 필요하므로
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)

bfs(1, V)