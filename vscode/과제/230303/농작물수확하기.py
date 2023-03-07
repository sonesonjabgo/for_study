T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    ans = 0
    m = N//2
    s = e = m

    for i in range(N):
        for j in range(s, e+1):
            ans += data[i][j]

        if i < m:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print(f'#{tc} {ans}')