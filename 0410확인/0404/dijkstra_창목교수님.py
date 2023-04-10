V, E = map(int, input().split())
graph = [[0xffffffffff] * V for _ in range(V)]

# start로 부터 각 정점을 가는 비용을 가지는 배열 반환
def dijkstra(start, U):
    weight = [0xffffffffff] * V
    # 시작 정점 설정하기
    weight[start] = 0 # 시작정점에서 시작정점까지 비용은 0

    # 각 정점까지 가는 비용 중에 가장 작은 비용이 드는 정점을 선택 >> 모든 정점이 선택될 때 까지 반복
    while len(U) < V:
        min_v = 0xffffffffff
        min_idx = 0
        for i in range(V):
            # i번 노드까지 가는 비용이 확정되지 않은 정점들 중에서
            # weight[i] 예네들 중에 최솟값 찾기
            if i not in U and weight[i] < min_V:
                min_v = weight[i]
                min_idx = i
            
            U.add

            for i in range(V):
    return weight