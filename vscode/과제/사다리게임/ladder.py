import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    ladder = []
    for _ in range(100):
        ladder1 = list(map(int, input().split()))
        ladder.append(ladder1)

    # 상 방향은 필요없음 하 우 좌
    col = [0, 1, -1]
    row = [1, 0, 0]

    # 현재 위치
    dir = 0 # 현재 방향 아래로
    curi, curj = 0, 0  # 초기 위치

    for i in range(100):
        if ladder[0][i] != 1: # 시작점이라면 시작
            continue
                # 아래 방향으로 내려가야 함
            for j in range(100):
                ladder[j][i] -= 1
                for k in range(1,3):
                    nexti = i + col[k]  # 현재 0,0 우방향
                    nextj = j + row[k]

print('gg')


