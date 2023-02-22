def preorder(T):
    global count
    if T == 0:
        return
    count += 1
    preorder(tree[0][T])
    preorder(tree[1][T])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    tree = [[0]*(E+1+1) for _ in range(2)]
    data = list(map(int, input().split()))
    for i in range(0, E*2, 2):
        p, c = data[i], data[i+1]
        if not tree[0][p]: # 왼쪽 자식 공간이 비었다면
            tree[0][p] = c
        else:
            tree[1][p] = c
    # print(tree)
    count = 0
    preorder(N)
    print(f'#{tc} {count}')