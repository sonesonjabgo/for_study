def push(n):
    global heapcount
    heapcount += 1
    heap[heapcount] = n

    current = heapcount
    parent = current // 2
    while heap[parent] > heap[current]:
        heap[parent], heap[current] = heap[current], heap[parent]
        current = parent
        parent = current // 2



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    heap = [0] * (N+1)
    heapcount = 0

    for i in data:
        push(i)
    # print(heap)
    parent = heapcount // 2
    current = heapcount
    result = 0
    while current // 2 != 0:
        result += heap[parent]
        current = parent
        parent = current // 2
    print(f'#{tc} {result}')