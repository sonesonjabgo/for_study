'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
V, E = map(int, input().split())
adj = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    a, b, w = map(int, input().split())
    adj[a][b] = w
    adj[b][a] = w
############################ 인접행렬 완성
def prim(graph, V):
    # MST를 만들어가는 과정
    mst = set() # mst에 포장된 노드를 넣어주는 set
    # 강의 자료에 .. pi와 key에 해당하는 데이터는
    # pi : '어느 정점으로부터 선택되었나'를 저장하는 값
    # weight : 해당 정점을 선택하는 가중치
    pi = [None] * (V+1)
    weight = [0xffffffff] * (V+1)
    # 시작정접 잡아주기
    weight[start] = 0
    # 최소 가중치를 가지는 정점을 선택하는 것을 반복
    # >> 모든 정점이 선택될 때 까지 반복
    while len(mst) < V + 1:
        # 최소 가중치 선택하기
        min_v = 0xffffffff
        min_idx = 0
        # 아직 선택되지 않은 노드이면서 최소 가중치면 선택
        for i in range(V+1):
            if i not in mst and weight[i] < min_v