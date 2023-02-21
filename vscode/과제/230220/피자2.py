def is_empty():
    if front == rear:
        return True
    return False

def is_full():
    if (rear+1) % (N+1) == front:
        return True
    return False

def enQueue(data):
    global rear, cnt
    if not is_full():
        rear = (rear + 1) % (N+1)
        # 원형큐가 돌면서 큐가 비어있는 경우가 아닐 때
        # rear가 front랑 같아지면 안되기 때문에
        # 공간을 하나 더 만들어준다.
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
    queue = [0] * (N+1)
    # 화덕의 공간의 수는 N이지만 +1을 해주는 이유는
    # 원형큐를 사용하기 때문에 엔큐 디큐하는 과정에서 front에 있는 공간에 rear가 오면 안된다.
    # 디큐를 하는 경우는 반복문이 돌아가면서 치즈의 수를 줄이는데 0이 되는 경우에 디큐된다.

    front = rear = 0 # 원형 큐를 사용할 것임
    cnt = 0
    # cnt는 while문을 끝내기 위함인데
    # 아래 올 while 반복문은 화덕이 돌아가면서 치즈를 녹이고 치즈가 다 녹은 피자를 꺼내고
    # 그 자리에 다음 피자의 치즈 수와 피자의 인덱스를 튜플로 넣어주기 위함이다.
    # 우리가 구해야 할 값은 마지막으로 꺼내지는 피자의 인덱스이다
    # cnt는 남아있는 피자의 수이다.
    # 위의 선언한 엔큐 디큐 함수가 cnt를 1씩 더해주거나 빼주거나 한다.
    for i in range(N): # 처음 화덕의 빈 공간에 빈 공간의 수 만큼 피자를 넣어줌
        enQueue((pizza[i],i))
        # 피자의 치즈 수와 해당 피자가 몇 번 인덱스인지 필요하기 때문에
        # 튜플로 묶어 엔큐
    num = N
    # num을 N으로 해주는 이유는 바로 위의 for문을 통해 i값인 인덱스로 넣어진 숫자가
    # N-1까지기 때문에 다음 들어갈 피자의 인덱스를 기록하기 위해 N으로 설정
    while cnt > 1:
        cheese, idx = deQueue() # 피자를 꺼냈다
        # 위에 for문을 통해 화덕에 저장해놓은 피자 중
        # 가장 먼저 저장한 값이 나온다.
        if cheese//2 != 0:
            enQueue((cheese // 2, idx))
            # 피자를 꺼내봤는데 치즈가 0이 아닌 경우 다시 넣어줌
        else:
            # 한 바퀴를 돌았을 때 치즈는 //2 된다
            # 그 값이 0이라면 피자를 꺼내고 다음 대기하고 있는 피자를 넣어야 함
            # 다녹았으니 꺼내기
            if num < M - 1:  # num은 인덱스 값,
                # 위에서 pizza 변수에 받았던 값의 최대 인덱스보다 커지면 안됨
                enQueue((pizza[num], num))  # 위와 같이 기다리던 피자를 치즈 수와 인덱스랑 같이 넣어준다.
                num += 1
                # 위의 디큐를 통해 front값이 옮겨 가면서 (front 현재 1)
                # 그 자리에 다음 피자를 넣을 수 있게 됐다.


    print(f'#{tc} {deQueue()[1]+1}')

