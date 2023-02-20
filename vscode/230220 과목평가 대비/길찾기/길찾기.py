import sys
sys.stdin = open("input.txt", "r")

def dfs(start):
    stack = []
    visited = [0] * 100
    stack.append(start)
    visited[start] = 1
    result = []


    while stack:
        cur = stack[-1]
        for i in range(1, 100):
            if arr[cur][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                result.append(i)
                break
        else:
            stack.pop()

    return result

for _ in range(10):
    tc, N = map(int, input().split())
    arr = [[0] * 100 for _ in range(100)]

    data = list(map(int, input().split()))
    for i in range(0, len(data), 2):
        arr[data[i]][data[i+1]] = 1
    result = dfs(0)
    # print(result)
    if 99 in result:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
