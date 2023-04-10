# 간선 가중치가 작은거 부터 선택하기
# 만약 간선을 선택하려는데 사이클이 생기면 해당 간선은 선택 X

V, E = map(int, input().split())
graph = []
for _ in range(E):
    a, b, weight = map(int, input().split())
    graph.append((a,b,weight))

graph.sort(key=lambda x:x[2])
mst = set()
###################################
# 사이클이 생기는 걸 확인하기 위해서 서로소 집합을 활용합니다.
p = [x for x in range(V+1)]
def find_set(x): # x의 집합의 대표를 반환
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

def union(x,y):
    p[find_set(y)] = find_set(x)




for i in range(E):
    # 작은 거 선택해서 mst에 넣어줄건데
    # 같은 집합이 아니라면 선택 (=사이클이 생기지 않는다면)
    if graph[i][0] == find_set(graph[i][1]):
        continue
    mst.add(graph[i])
    union(graph[i][0], graph[i][1])