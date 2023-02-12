arr = [[1,2,3],[4,5,6],[7,8,9]]
n = len(arr)
m = len(arr[0])
# 3 * 3 행렬 (n * m)
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

# 행 우선 순회
# for i in range(n):
#     for j in range(m):
#         print(arr[i][j])

# 열 우선 순회
for i in range(m):
    for j in range(n):
        print(arr[j][i], end=' ')

print()
# 지그재그 순회
# 짝수 인덱스일 때는 정방향
# 홀수일 때는 역방향
for i in range(n):
    for j in range(m):
        if i % 2 == 0: # 짝수일 때
            print(arr[i][j], end=' ')
        else:
            print(arr[i][m-j-1], end=' ')

