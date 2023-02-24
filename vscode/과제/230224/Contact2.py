def bfs(T):
    queue = [T]
    visited = [0] * 101
    rst = []
    while queue:
        q = queue.pop(0)
        if not visited[q]:
            visited[q] = 1
            if ad_list[q]:
                for j in ad_list[q]:
                    queue.append(j)
            else:
                rst.append(q)
    return rst




for tc in range(1, 11):
    N, T = map(int, input().split())  # 데이터의 길이, 시작점
    data = list(map(int, input().split()))

    ad_list = [[] for _ in range(101)]

    for i in range(0, N, 2):
        ad_list[data[i]].append(data[i + 1])

    # print(ad_list)
    print(bfs(T))