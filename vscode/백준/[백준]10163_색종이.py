import sys

N = int(sys.stdin.readline())
mina, minb = 1001, 1001
maxs, maxe = 0, 0
arr = [[-1] * 1001 for _ in range(1001)]

for k in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())

    for i in range(a, a+c):
        for j in range(b, b+d):
            arr[i][j] = k
    mina, minb = min(a, mina), min(b, minb)
    maxs, maxe = max(a+c, maxs), max(b+d, maxe)

cnt = [0] * N

for k in range(N):
    for i in range(mina, maxs):
        for j in range(minb, maxe):
            if arr[i][j] == k:
                cnt[k] += 1


for i in cnt:
    print(i)