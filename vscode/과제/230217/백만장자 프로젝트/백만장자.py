T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    fit = 0
    max_price = price[-1]
    for i in range(N-2, -1, -1):
        if max_price < price[i]:
            max_price = price[i]
        else:
            fit += max_price - price[i]
    print(f'#{tc} {fit}')

