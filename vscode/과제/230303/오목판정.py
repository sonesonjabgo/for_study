T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [input() for _ in range(N)]

    result = 'NO'
    # 우 하 우하 좌하
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]

    for i in range(N):
        for j in range(N):
            if data[i][j] == 'o':
                for k in range(4):
                    cnt = 0
                    ci = i
                    cj = j
                    while 0 <= ci < N and 0 <= cj < N and data[ci][cj] == 'o':
                        cnt += 1
                        ci = ci + dr[k]
                        cj = cj + dc[k]
                    if cnt >= 5:
                        result = 'YES'

    print(f'#{tc} {result}')