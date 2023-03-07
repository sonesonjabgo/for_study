T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()

    rst = 'Possible'
    time = gugu = i = 0
    while i < N and time <= lst[-1]:
        if lst[0] == 0:
            rst = 'Impossible'
            break
        time += 1
        if time % M == 0:
            gugu += K
        if time == lst[i]:
            if gugu:
                # rst = 'Possible'
                gugu -= 1
                i += 1

            else:
                rst = 'Impossible'
                break

    print(f'#{tc} {rst}')