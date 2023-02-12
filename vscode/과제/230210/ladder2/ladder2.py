import sys
sys.stdin = open("input.txt", "r")

# 하 좌 우
d1 = [1, 0, 0]
d2 = [0, -1, 1]

for _ in range(10):
    minimum = 10000  # 100*100칸이니 최대 이동해도 10000은 넘지 않음
    min_idx = 0
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    resultlst = []
    for i in range(100):
        result = 0
        if arr[0][i] == 1: # 첫 줄에 1인 것에서만 시작해야 하기 때문
            dir = 0 # 현재 방향 // 현재 위치 r,c 에 r + d1[dir] 이런 식으로 활용
            r, c = 0, i # 첫 시작 0,0
            while r < 99: # r 이 98이라는 것은 도착점 바로 직전에 위치하다는 것
            # 99 일 때는 아래 방향으로 움직이는 것을 막기 위해 (인덱스 넘어감)
                if dir == 0: # 현재 방향이 0일 때
                # 좌우에 길이 있는 지 파악해야 한다.
                # 그리고 없으면 아래 방향으로 진행
                    if c > 0 and arr[r][c-1] == 1:
                    # c > 0 은 범위를 넘어가는 것을 방지
                    # 1 이라는 것은 길이 있다는 것
                        dir = 1
                    elif c < 99 and arr[r][c+1] == 1:
                        dir = 2
                else: # 좌나 우 방향으로 진행하고 있을 때
                # 더 이상 좌나 우로 갈 길이 없고 아래쪽으로 향해야 하는 지 확인해야 함
                # 하지만 조건에 양 옆으로 길이 난 경우는 없으니
                # 아래 쪽으로 길이 있는 지만 확인하면 됨
                    if arr[r+1][c] != 0:
                        dir = 0
                r = r + d1[dir]
                c = c + d2[dir]
                result += 1 # 이동할 때 마다 1 상승
                # r과 c를 다시 선언하므로써 현재 위치를 바꿔주는 것

    # ladder1 문제와 다른 점은 목적지가 2인 곳에 도착하는 것이 아니라
    # 마지막 지점에 도달하는 데 까지 얼마나 이동을 해야하는 지가 궁금한 것
    # 그 숫자들의 min값의 i를 가져와야 함
            if result < minimum:
                minimum = result
                min_idx = i
    print(f'#{T} {min_idx}')