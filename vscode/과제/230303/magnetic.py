# 불을 끈 상태에서 시작
# 1이면 불을 켜고 2를 만나면 카운트 올리고 불을 끈다

for tc in range(1, 11):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        light = False
        for j in range(N):
            if data[j][i] == 1:
                light = True

            elif light and data[j][i] == 2:
                cnt += 1
                light = False

    print(f'#{tc} {cnt}')