# 선형큐의 사용한 앞 공간을 쓰기 위해 
# 모듈러 연산으로 다시 앞으로 돌려주는 것
N = 10
queue = [None] * N
front = rear = 0


def is_empty(): # 큐가 비었으면 True를 반환 아니라면 False를 반환
    # front랑 rear랑 같으면 비어있는거
    if front == rear:
        return True
    return False

# is_full() : 큐가 가득 찼는지 확인하는 함수
def is_full():
    # 원형큐에서는 rear가 움직일 다음 칸이 front의 위치라면 full 상태
    if (rear+1) % N == front:
        return True
    return False

def enQueue(data):
    global rear
    if not is_full(): # 데이터가 가득차지 않은 경우에만 들어가야 하기에
        rear = (rear + 1) % N
        queue[rear] = data
    else:
        raise IndexError('큐가 가득 찼다.')
    
def deQueue():
    global front
    if not is_empty():
        front = (front + 1) % N
        return queue[front]
    else:
        raise IndexError('큐가 비었다.')