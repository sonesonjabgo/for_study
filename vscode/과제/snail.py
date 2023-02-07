T = int(input())
for t in range(1, T+1):
    N = int(input())
    snail = [[0 for _ in range(N)] for _ in range(N)]
    # 우 하 좌 상 순으로
    dj = [1, 0, -1, 0]
    di = [0, 1, 0, -1]

    dir = 0           # 현재 방향 (1, 0) 우방향
    curi, curj = 0, 0 # 초기 위치

    for num in range(1, N*N+1):
        snail[curi][curj] = num

        nexti = curi + di[dir] # 현재 0,0 우방향
        nextj = curj + dj[dir]
        if nexti < 0 or nexti >= N or nextj < 0 or nextj >= N or snail[nexti][nextj] != 0:
        # 다음 위치가 범위를 벗어나거나                                해당 인덱스에 숫자를 입력했다면
            dir = (dir + 1) % 4 # 1을 더해 방향을 바꾼다
            # 그리고 4로 %해서 0,1,2,3 안에서 돌도록 만든다
            # 넘어가면 di, dj에서 인덱스 에러

        curi += di[dir]
        curj += dj[dir]

    print(f'#{t}')
    for k in snail:
        print(*k)