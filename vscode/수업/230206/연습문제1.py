# 델타 이동 연습 문제 1
arr = [[x for x in range(n,n+5)] for n in range(1,6)]
# arr = [
#     [1,2,3,4,5],
#     [2,3,4,5,6],
#     [3,4,5,6,7],
#     [4,5,6,7,8],
#     [5,6,7,8,9]
# ]

# 상하좌우
dr = [-1, 1, 0, 0] # 행 변화량
dc = [0, 0, -1, 1] # 열 변화량
# 행, 열의 변화량 쌍 (상하좌우)
d = [(-1,0),(1,0),(0,-1),(0,1)]
r, c = 2, 2
for a in range(4): # 4방향이니까 4
    print(arr[r + dr[a]][c + dc[a]])