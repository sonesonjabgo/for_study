import sys

T = 1001
arr = [[0] * T for _ in range(T)]
N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

color = 1
for paper in data:
    a, b, c, d = paper
    s = a + c
    e = b + d
    for i in range(a, s):
        for j in range(b, e):
            arr[i][j] = color
    color += 1

check = 1
while check <= N:
    cnt = 0
    for i in range(T):
        for j in range(T):
            if arr[i][j] == check:
                cnt += 1
    print(cnt)
    check += 1