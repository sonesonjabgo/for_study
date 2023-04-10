'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs1(v, k):  # 중복없이 빠짐없이
    visited[v] = 1 # 중복방지용
    print(v)
    # for w in adjL[v]:  # v와 인접하고
    #     if visited[w] == 0: # 방문한 적이 없는 w가 있으면
    #         dfs1(w,k)
    for w in range(1, k+1):
        if adjM[v][w]==1 and visited[w]==0:
            dfs1(w, k)



V, E = map(int, input().split())
arr = list(map(int, input().split()))

visited = [0] * (V+1)   # 중복방지용

adjM = [[0]*(V+1) for _ in range(V+1)] # 인접행렬
adjL = [[] for i in range(V+1)]

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1    # 방향이 없는 경우
    adjL[n1].append(n2)
    adjL[n2].append(n1) # 방향이 없는 경우
    
print()

dfs1(1, V)