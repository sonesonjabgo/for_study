import sys
sys.stdin = open("sample_input.txt", "r")

def graph(V, E):
    nod = [list(map(int, input().split())) for _ in range(E)]

    arr = [[0] * (V+1) for _ in range(V+1)]
    # 노드의 연결을 기록해두기 위함임.
    # 노드에 적혀있는 인덱스 접근을 위해 V에 +1을 해준다.

    # nod[0][0] 이 출발
    # nod[0][1] 이 도착
    for i in range(E):
        arr[nod[i][0]][nod[i][1]] = 1
        # 1 4 의 경우 1에서 4로 가는 경로가 있다라는 것을 표시하는 것이여서
        # arr[1][4]에 1을 선언하는 것
    return arr

def dfs(arr, tar):
    stack = []
    visited = [0] * (V+1)
    start, end = tar[0], tar[1]
    stack.append(start)
    visited[start] = 1
    result = ''

    while stack:
        cur = stack[-1]
        for i in range(1, V+1):
            if arr[cur][i] and not visited[i]:
                stack.append(i)

                visited[i] = 1
                result += str(i) + ' '
                break
        else:
            stack.pop()

    return result

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = graph(V,E)
    tar = list(map(int, input().split()))
    result = dfs(arr, tar)
    if str(tar[1]) in result:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')