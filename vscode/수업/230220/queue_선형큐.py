# 마치 큐인 것 처럼 동작하는 리스트 만들기
N = 10
queue = [None] * N

front = rear = -1
# 큐의 현재 맨 앞 요소와 맨 뒷 요소의 인덱스를 가지고 있는 변수
# front : 맨 앞 요소의 -1 인덱스
# rear : 맨 뒷 요소의 인덱스


# enQueue(data) : 큐의 맨 뒤에 data 삽입 
def enQueue(data):
    global rear
    if not is_full(): # 데이터가 가득차지 않은 경우에만 들어가야 하기에
        rear += 1
        queue[rear] = data
    else:
        raise IndexError('큐가 가득 찼다.')
# deQueue() : 큐의 맨 앞에서 데이터 반환 및 삭제
def deQueue():
    global front
    if not is_empty():
        front += 1
        return queue[front]
    else:
        raise IndexError('큐가 비었다.')
#### 디큐를 하고나면 front가 옮겨가는데 그러면 큐 리스트에는 값이 남아있는건가?
#### 그러면 잘못된 포화상태 인식 문제가 왜 생겨나는 것 인가

# is_empty() : 큐가 비었는지 확인하는 함수
def is_empty(): # 큐가 비었으면 True를 반환 아니라면 False를 반환
    # front랑 rear랑 같으면 비어있는거
    if front == rear:
        return True
    return False


# is_full() : 큐가 가득 찼는지 확인하는 함수
def is_full():
    # 선형 큐에서 full이란, rear가 큐의 마지막 인덱스를 가리키고 있을 때
    if rear == N-1:
        return True
    return False

# A, B, C, D, E
enQueue('A')
enQueue('B')
enQueue('C')
enQueue('D')
enQueue('E')
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())

## 원형큐와 선형큐의 시작점 차이의 이유
# 0번 인덱스를 사용하기 위함인가?
