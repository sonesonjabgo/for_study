T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0

    for i in range(N):
        for j in range(M):
            cnt = num = data[i][j]
            for k in [(1,0),(0,1),(-1,0),(0,-1)]:
                for q in range(1, num+1):
                    ni = i + k[0] * q
                    nj = j + k[1] * q
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += data[ni][nj]
            if cnt > max_cnt:
                max_cnt = cnt

    print(f'#{tc} {max_cnt}')