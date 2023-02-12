arr = [
    [1,2,3,4,5],
    [2,3,4,5,6],
    [3,4,5,6,7],
    [4,5,6,7,8],
    [5,6,7,8,9]
]
# 상 하 좌 우
d1 = [-1, 1, 0, 0]
d2 = [0, 0, -1, 1]
count = 0
for i in range(5):
    for j in range(5):
        for k in range(4): # 4방향
            if i+d1[k] >= 0 and i+d1[k] < 5 and j+d2[k] >= 0 and j+d2[k] < 5:
                num = arr[i+d1[k]][j+d2[k]] - arr[i][j]
                if num < 0:
                    num = -num
                count += num
print(count)