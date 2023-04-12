# 해당 코드는 큐를 사용한 것
# 리스트의 pop과 세트의 add를 활용하는 것은 시간이 많이 걸림
# 기본 조건인 백만 아래의 자연수들을 저장할 공간을 만들어주고 (checked)
# 검사해야 할 숫자가 사용됐는 지 확인한다.

def bfs(N, M):
    # queue = [(N, 0)]
    # checked = set()
    # checked.add(N)
    checked = [0] * 1000001
    # 선형큐 선언
    queue = [(0, 0)] * 1000000
    front = -1
    rear = -1
    rear += 1
    queue[rear] = (N, 0)
    while queue:
        front += 1
        num, cnt = queue[front]
        # num, cnt = queue.pop(0)

        if num == M:
            return cnt
        # if num >= 1000000 or num < 0:
        #     continue
        # 네 가지 연산을 수행해서 결과를 queue 넣어주기

        tmp = num + 1
        if (0 < tmp <= 1000000) and not checked[tmp]:
            rear += 1
            # queue.append((num + 1, cnt + 1))
            # checked.add(num + 1)
            queue[rear] = (tmp, cnt + 1)
            checked[tmp] = 1

        tmp = num - 1
        if (0 < tmp <= 1000000) and not checked[tmp]:
            rear += 1
            # queue.append((num - 1, cnt + 1))
            queue[rear] = (tmp, cnt + 1)
            checked[tmp] = 1

        tmp = num * 2
        if (0 < tmp <= 1000000) and not checked[tmp]:
            rear += 1
            # queue.append((num * 2, cnt + 1))
            queue[rear] = (tmp, cnt + 1)
            checked[tmp] = 1

        tmp = num - 10
        if (0 < tmp <= 1000000) and not checked[tmp]:
            rear += 1
            # queue.append((num - 10, cnt + 1))
            queue[rear] = (tmp, cnt + 1)
            checked[tmp] = 1
    return -1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 주어진 노드는 +1, -1, *2, -10
    # 시작점 N에 대하여 노드 연결을 해주어야 함
    # N == 2이면 3, 1, 4, -8 이건 가중치. 일일히 다 적어줄 것이 아니고 
    # 해당 노드로 현 위치가 옮겨가게 된다면 가중치를 구하는 식으로 처리

    result = bfs(N, M)
    print(f'#{tc} {result}')
