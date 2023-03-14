# 한 지점 기준으로 8x8 이동시키고 색깔 칠해지는 기준 틀리면 카운트.
N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]


result = []
for i in range(N):
    for j in range(M):
        # i와 j를 8번 하나씩 옮길건데 범위가 넘어가면 안됨.
        # 범위가 넘어가는 경우가 있는 지 확인 먼저
        if i+7 < N and j+7 < M:
            draw1 = 0
            draw2 = 0
            for a in range(i, i+8):
                for b in range(j, j+8):
                    if (a + b) % 2 == 0:
                        if data[a][b] != 'B':
                            draw1 += 1
                        if data[a][b] != 'W':
                            draw2 += 1
                    else:
                        if data[a][b] != 'W':
                            draw1 += 1
                        if data[a][b] != 'B':
                            draw2 += 1
            result.append(draw1)
            result.append(draw2)
# print(result)
print(min(result))