# # 100번째 행에 원소의 값이 2인 것이 도착 x 지점
# # x부터 위로 올라간다고 생각하면 편하다
# # x의 좌표 r, c 의 4방향 확인해서 그 중 1이 있는지 확인
# # 방향 중 2개면 위로 방향 중 3개면 좌나 우값이 1인 곳으로 이동

# T = int(input())
# for t in range(1, T+1):
#     ladder = []
#     for _ in range(100):
#         ladder1 = list(map(int, input().split()))
#         ladder.append(ladder1)

#     # 상 우 좌 시계방향
#     dr = [-1, 0, 0]
#     dc = [0, -1, 1]

#     for i in range(100):
#         if ladder[99][i] == 2:
#             dir = 0
#             r, c = 99, i
#             # 현재 방향 위쪽으로
#             # 정답의 좌표 -1, i
#             while r > 0:
#                 # 현재 방향이 위쪽 방향을 향할 때 좌우를 봐야함
#                 if dir == 0:
#                     if

###################################

# 수업 때 풀이
# 처음부터 내려가는 식의 풀이
# 내려가는 것은 아래쪽, 좌측, 우측 방향이 필요함

# 한칸 씩 내려가는 방법
# 델타

import sys
sys.stdin = open("input.txt", "r")

T = 10
for _ in range(1, T + 1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 시작 점 찾기 : 0번 행에서 1인 인덱스 찾기
    # 하 좌 우
    dr = [1,0,0]
    dc = [0,-1,1]

    for i in range(100):
        if ladder[0][i] == 1:
        # 시작 점 마다 사다리 타기 시작
            dir = 0 # 아래방향 시작
            r, c = 0, i
            # 한 칸 씩 이동하기를 반복 >>> 목적지 도착하기 전 까지
            # = r 이 99가 될 때 까지 반복
            while r < 99:
                # 특정한 상황에서 방향을 바꿔주어야 함
                # 1. 아래쪽으로 내려올 때
                if dir == 0:
                    # 좌우에 1이 있으면 방향전환
                    if c > 0 and ladder[r][c-1] == 1: # c > 0 은 범위를 넘어가는 경우 방지
                        dir = 1
                    elif c < 99 and ladder[r][c+1] == 1: # c < 99 는 범위를 넘어가는 경우 방지
                        dir = 2
                # 2. 왼쪽 or 오른쪽으로 이동할 때
                    # 아래쪽에 1이 있으면 방향 전환
                else:
                    # 도착지가 1,2인 경우가 있으니 0이 아니면으로 검사
                    if ladder[r+1][c] != 0:
                        dir = 0

                # 현재 방향으로 한 칸 씩 이동
                r += dr[dir]
                c += dc[dir]

            # r = 99, c = x
            if ladder[r][c] == 2:
                # i가 정답
                result = i
                break # 더 이상 반복문 돌 필요 없다.
    print(f'#{tc} {result}')
# 해당 행이나 열 쭉 내려가고 옆길 있을 때 그 방향으로 쭉 가는 방법
# while