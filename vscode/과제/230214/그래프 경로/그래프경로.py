import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    data = ''
    for _ in range(E):
        data += input() + ' '
    data = list(map(int, data.split()))
    start, end = map(int, input().split())
    for i in range(0, E*2, 2):
        a, b = data[i], data[i+1]
        adj[a][b] = 1
    ####### 인접행렬 완성 #######
    # print (f'V = {V} E = {E} start = {start} end = {end}')
    # for arr in adj:
    #     print(*arr)
    def dfs(start):
        # stack을 이용해서 저장 (경로 저장용)
        stack = []  # 이름만 스택인 리스트 만듦
        # 되돌아 가는 건 괜찮지만 재방문은 막아야 함
        # visited 배열 만들기
        visited = [0] * (V + 1)
        stack.append(start)
        visited[start] = 1
        # print(start, end=' ')
        result = ''

        while stack:  # 스택이 비어있지 않으면 계속 반복
            current = stack[-1]  # 현재 내 위치 (현재 노드)
            # 현재 내 위치에서 연결된 노드를 확인
            for i in range(1, V + 1):
                if adj[current][i] and not visited[i]:
                    # 노드가 현재 노드와 연결되어있고 그 노드가 방문하지 않았는 지 확인
                    stack.append(i)
                    visited[i] = 1
                    result += str(i) + ' '
                    break  # 연결된 노드 찾기 중단
            else:  # for문 수행 중에 경로 발견 못함
                stack.pop()
            # 현재 위치에서 길이 없을 때 까지 위 코드 반복
        return result

    # 1번 노드부터 dfs 수행
    result = list(map(int, dfs(start).split()))
    # print(result)
    if end in result:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
    # print()