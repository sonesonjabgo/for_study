def deQueue():
    global front
    front = (front + 1) % N
    return queue[front]

# 값을 채운 원형 큐에
# 디큐를 해서 계속 값 돌아가게 하는 것
# 채우진 않음

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    front = 0
    for i in range(M):
        if i == M-1:
            print(f'#{tc} {deQueue()}')
        else:
            deQueue()
