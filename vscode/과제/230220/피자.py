def is_empty(): # 큐가 비었으면 True를 반환 아니라면 False 반환
    # front랑 rear랑 같으면 비어있는거
    if front == rear:
        return True
    return False

def is_full():  #
    # 원형큐에서는 rear가 움직일 다음칸이 front의 위치라면 full 상태
    if (rear+1) % (N+1) == front:
        return True
    return False

def enQueue(data):
    global rear, cnt
    if not is_full():
        rear = (rear + 1) % (N+1)
        queue[rear] = data
        cnt += 1
    else:
        raise IndexError('큐가 가득 찼습니다.')

def deQueue():
    global front,cnt
    if not is_empty():
        front = (front + 1) % (N+1)
        cnt -= 1
        return queue[front]
    else:
        raise IndexError('큐가 비었습니다.')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    queue = [0] * (N+1) # 화덕
    front = rear = 0
    cnt = 0
    for i in range(N):
        enQueue((pizza[i],i))
    num = N
    while cnt > 1:
        cheese, idx = deQueue()
        if cheese//2 == 0:
            # 다녹았으니 꺼내기

            if num < M-1:
                enQueue((pizza[num],num))
                num += 1
        else:
            enQueue((cheese//2, idx))

    print(f'#{tc} {deQueue()[1]+1}')

