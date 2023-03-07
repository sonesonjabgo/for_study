T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]

    # 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    max_fly = 0
    for i in range(N):
        for j in range(N):
            ci = i
            cj = j
            fly = data[ci][cj]
            for k in range(4):
                ni = ci + dr[k]
                nj = cj + dc[k]
                for _ in range(1, M):
                    if 0 <= ni < N and 0 <= nj < N:
                        fly += data[ni][nj]
                        ni += dr[k]
                        nj += dc[k]
            if fly > max_fly:
                max_fly = fly

    # 좌상 우상 우하 좌하
    pr = [-1, 1, 1, -1]
    pc = [-1, -1, 1, 1]

    for i in range(N):
        for j in range(N):
            ci = i
            cj = j
            fly = data[ci][cj]
            for t in range(4):
                ni = ci + pr[t]
                nj = cj + pc[t]
                for _ in range(1, M):
                    if 0 <= ni < N and 0 <= nj < N:
                        fly += data[ni][nj]
                        ni += pr[t]
                        nj += pc[t]
            if fly > max_fly:
                max_fly = fly

    print(f'#{tc} {max_fly}')