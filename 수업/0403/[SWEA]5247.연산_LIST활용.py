def bfs(N, M):
    queue = [(N, 0)]
    checked = set()
    checked.add(N)
    while queue:
        num, cnt = queue.pop(0)

        if num == M:
            return cnt
        if num >= 1000000 or num < 0:
            continue
        # 네 가지 연산을 수행해서 결과를 queue 넣어주기
        if num + 1 not in checked:
            queue.append((num + 1, cnt + 1))
            checked.add(num + 1)
        if num - 1 not in checked:
            queue.append((num - 1, cnt + 1))
            checked.add(num - 1)
        if num * 2 not in checked:
            queue.append((num * 2, cnt + 1))
            checked.add(num * 2)
        if num - 10 not in checked:
            queue.append((num - 10, cnt + 1))
            checked.add(num - 10)
    return -1
    # 4갈래로 계산을 하는데 모든 노드를 검사하게 되면 수가 어마어마하게 많아져서
    # 이미 나왔던 숫자는 더 이상 연산하지 않도록 해야함
    # 먼저 연산된 숫자가 찾는 숫자라면 연산 횟수를 리턴
    # 왜냐하면 그 전에 그 숫자가 나왔다면 cnt가 더 적은 수이기 때문에
    # 큐에 연산 값과 연산 횟수를 저장하고
    # checked 튜플에 이미 나온 숫자를 저장한다.
    # 그리고 사전 조건인 일백만 이하의 자연수 조건을 검사하고
    # 4갈래의 연산들이 checked에 있는 지 확인


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 주어진 노드는 +1, -1, *2, -10
    # 시작점 N에 대하여 노드 연결을 해주어야 함
    # N == 2이면 3, 1, 4, -8 이건 가중치. 일일히 다 적어줄 것이 아니고
    # 해당 노드로 현 위치가 옮겨가게 된다면 가중치를 구하는 식으로 처리
    result = bfs(N, M)
    print(f'#{tc} {result}')