for _ in range(1, 11):
    tc = int(input())
    data = list(map(int,input().split())) + [0] * 100000

    front = -1
    rear = 7
    while data[rear] != 0:
        for i in range(1, 6):
            front += 1
            if data[front] - i <= 0:
                rear += 1
                data[rear] = 0
                break
            else:
                rear += 1
                data[rear] = data[front] - i
    print(f'#{tc}', *data[rear-7:rear+1])
