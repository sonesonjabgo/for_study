T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]

    heap = [0] * (N+1)
    for i in data:
        heap[i[0]] = i[1]

    if N % 2:
        j = -1
    else:
        j = 0

    for i in range(N, 0, -1+j):
        if i // 2 and heap[i // 2] == 0:  # 부모노드가 존재하고 부모노드에 값이 채워지지 않았을 때
            if (i-1) // 2 == i // 2:
                heap[i//2] = heap[i] + heap[i-1]
                j = -1
            else:
                heap[i//2] = heap[i]

    print(f'#{tc} {heap[L]}')