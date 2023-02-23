import sys
sys.stdin = open("input.txt", "r")

def inorder(T):
    if T == 0:
        return
    inorder(tree[0][T])
    order.append(T)
    inorder(tree[1][T])



for tc in range(1, 11):
    N = int(input())
    data = [input().split() for _ in range(N)]
    # print(data)
    tree = [[0] * (N+1) for _ in range(2)]
    mydict = {}
    for i in data:
        if len(i) == 4:
            tree[0][int(i[0])] = int(i[2])
            tree[1][int(i[0])] = int(i[3])
        if len(i) == 3:
            tree[0][int(i[0])] = int(i[2])
        mydict[int(i[0])] = i[1]
    # print(mydict)
    order = []
    inorder(1)
    # print(order)
    print(f'#{tc}', end=' ')
    for i in order:
        print(mydict[i], end='')
    print()