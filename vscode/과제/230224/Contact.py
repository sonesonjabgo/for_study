def solve(N, num):
    visited[N] = 1
    if not ad_list[N]:
        return [num, N]
    # and ad_list[N]:
    #    print(*ad_list[N])
    my_num = [num, N]
    for i in ad_list[N]:
        if not visited[i]:
            tmp_num, node_num = solve(i, num + 1)
            if my_num[0] < tmp_num:
                my_num = [tmp_num, node_num]
            elif my_num[0] == tmp_num:
                my_num[1] = max(my_num[1], node_num)
    return my_num


for tc in range(1, 11):
    N, T = map(int, input().split())  # 데이터의 길이, 시작점
    data = list(map(int, input().split()))

    ad_list = [[] for _ in range(101)]

    for i in range(0, N, 2):
        ad_list[data[i]].append(data[i + 1])

    # print(ad_list)
    visited = [0] * 101
    max_num = solve(T, 0)
    # T를 넣으면 ad_list[T]의 요소들을 출력하고
    # 그 요소들을 K로 두고 ad_list[K]를 출력한다
    # 그 과정을 계속 진행하고 마지막에 출력되는 것 중에 최대값을 찾는다.
    # 재귀함수를 사용하는데
    # T로 들어갈 노드의 개수를 모른다.
    print(f'#{tc} {max_num[1]}')