import sys
sys.stdin = open("input.txt", "r")

while True:
    try:
        V = 99 # 정점의 번호는 0 ~ 99
        tc, E = map(int, input().split())
        data = list(map(int,input().split()))
        adj = [[0] * (V+1) for _ in range(V+1)] # 101 * 101 행렬 만듦
        # 노드끼리 연결되있는 것을 표현하려면 인덱스로 접근하는게 편함
        for i in range(0, E*2, 2):
            a, b = data[i], data[i+1]
            adj[a][b] = 1
    ########## 인접행렬 만듦 ######################

        def dfs(start):
            stack = []
            visited = [0] * (V + 1)
            stack.append(start)
            visited[start] = 1
            count = ''
            while stack:
                current = stack[-1]
                for i in range(V,0,-1):
                    if adj[current][i] and not visited[i]:
                        stack.append(i)
                        visited[i] = 1
                        count += ' ' + str(i)
                        break
                else:
                    stack.pop()
            count = count.split()
            if '99' in count:
                print(f'#{tc} 1')
            else:
                print(f'#{tc} 0')

        dfs(0)
    except EOFError:
        break