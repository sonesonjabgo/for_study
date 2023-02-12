# box의 인덱스마다 가장 높이 있는 박스가 제일 많이 내려가게 될 것임
# 각 인덱스마다 최고 값이 중력이 바뀌어서 바닥(len(box)-1)까지 내려가는 데 구하는 문제
# box = list(map(int, input().split()))
# [7, 4, 2, 0, 0, 6, 0, 7, 0]
box = [7, 4, 2, 0, 0, 6, 0, 7, 0]
# ans에 box의 각 인덱스(i)마다 len(box)-1 인덱스까지 이동하는 데 필요한 인덱스 구하기

ans = [0] * len(box)
for i in range(len(box)):
    count = 0
    for j in range(i+1, len(box)):
        if box[i] > box[j]:
            count += 1
    ans[i] = count
maxans = ans[0]
for k in ans:
    if k > maxans:
        maxans = k
print(maxans)