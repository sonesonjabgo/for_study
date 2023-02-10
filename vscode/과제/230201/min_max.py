T = int(input()) # 3
for t in range(1, T+1): # 1 2 3
    N = int(input()) # 5
    J = list(map(int, input().split())) #[477162, 658880, 751280, 927930, 297191]
    maxnum = J[0]
    minnum = J[0]
    for j in range(1, N): # 1 2 3 4
        if J[j] > J[j-1] and J[j] > maxnum: # J[1] > J[0]
            maxnum = J[j]
        elif J[j] < minnum:
            minnum = J[j]

    result = maxnum - minnum
    print(f'#{t} {result}')
