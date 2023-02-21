# 7 8  노드의 수 / 연결 노드 수 (간선)
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

# 먼저 노드의 정보를 받아서
# 인접 리스트를 만들어준다.
V, E = map(int, input().split())
data = list(map(int, input().split()))
adj_L = [0] * (V+1) # 0번은 안쓰고 1번부터 V번까지
# 이게 어떤 의미냐면
# adj_L[1] >> [3,4] 라면 1번 노드가 3번,4번 노드에 연결되어 있다는 뜻이다.
for i in range(0, E*2, 2):
    n1, n2 = data[i], data[i+1]
    adj_L[n1].append(n2)
    adj_L[n2].append(n1)
    # 인접리스트에 양방향으로 기록한 것임.

def bfs(N): # 노드 끝번 (V)