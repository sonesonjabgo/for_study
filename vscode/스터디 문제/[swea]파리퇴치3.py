T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    cnt_lst = []
    for i in range(N):
        for j in range(N):
            cnt = data[i][j]
            # 상 우 하 좌
            for k in [(-1,0),(0,1),(1,0),(0,-1)]:
                for a in range(1, M):
                    ni = i + k[0] * a
                    nj = j + k[1] * a
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += data[ni][nj]
            cnt_lst.append(cnt)

            cnt = data[i][j]
            # 대각선
            for k in [(-1,-1),(-1,1),(1,1),(1,-1)]:
                for a in range(1, M):
                    ni = i + k[0] * a
                    nj = j + k[1] * a
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += data[ni][nj]
            cnt_lst.append(cnt)


    print(f'#{tc} {max(cnt_lst)}')