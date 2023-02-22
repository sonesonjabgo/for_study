def inorder(T):
    if T == 0:
        return
    inorder(tree[0][T])
    nod.append(T)
    inorder(tree[1][T])


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # 높이를 구하고
    # 높이를 통해 트리의 최대 공간을 구하고
    # 그 곳에 맞는 인덱스에 맞는 값을 넣어준다.
    tree = [[0] * (N+1) for _ in range(2)]
    for i in range(1, N+1):
        if 2 * i > N:
            break
        tree[0][i] = 2 * i
        if 2 * i + 1 > N:
            break
        tree[1][i] = 2 * i + 1
    nod = []
    inorder(1)

    cnt = 1
    for i in nod:
        if i == 1:
            break
        else:
            cnt += 1
    num = N//2
    cnt2 = 1
    for i in nod:
        if i == num:
            break
        else:
            cnt2 += 1

    print(f'#{tc}',cnt, cnt2)