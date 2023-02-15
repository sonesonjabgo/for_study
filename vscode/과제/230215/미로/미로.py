import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, list(input().strip()))) for _ in range(N)]
    # print(arr)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                sr, sc = i, j # 출발 지점 인덱스 찾기

    # print(sr, sc)

    def dfs(sr, sc):
        stack = [(sr, sc)]
        visited = [[0] * N for _ in range(N)]

        visited[sr][sc] = 1
        while stack:
            # 현재 위치
            cr, cc = stack[-1]
            # 초기 top 은 시작 값
            if arr[cr][cc] == 3:
                return 1
            # top에서 이동할 수 있는 모든 경로 살펴보기
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상 하 좌 우 순으로
                nr = cr + dr
                nc = cc + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if not arr[nr][nc] and not visited[nr][nc]:  # 갈 수 있음
                        stack.append((nr, nc))
                        # 방문했음을 표시
                        visited[nr][nc] = 1
                        break
                    elif arr[nr][nc] == 3:
                        stack.append((nr, nc))
                        break
            else:
                stack.pop()
        return 0

    print(f'#{test_case} {dfs(sr, sc)}')