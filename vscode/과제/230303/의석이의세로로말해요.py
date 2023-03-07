T = int(input())
for tc in range(1, T+1):
    data = [input() for _ in range(5)]

    rst = ''
    for i in range(15):
        for j in range(5):
            if i < len(data[j]):
                rst += data[j][i]

    print(f'#{tc} {rst}')