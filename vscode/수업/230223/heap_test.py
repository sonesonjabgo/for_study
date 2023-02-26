# 완전 이진트리 >> 배열 형태에 저장 가능
# 최소힙 만들기
heap = [0] * (2**4)  # 높이 3짜리의 이진 트리를 저장할 수 있음
# 삽입과 삭제 : 마지막 자리를 알고 있어야 함
heapcount = 0           # 마지막 요소의 자리
def heap_push(data):    # heap에 요소 추가
    global heapcount
    # 마지막 요소의 뒤에 새로운 요소를 추가
    heapcount += 1
    heap[heapcount] = data
    # 새로 추가한 요소가 부모보다 작다면 교환 (교환 후에 부모가 더 크다면 계속 반복하기, 루트까지)
    parent = heapcount//2
    current = heapcount
    while heap[parent] > heap[current]:    # 부모가 더 크다면 자리 교환
        heap[parent], heap[current] = heap[current], heap[parent]
        current = parent
        parent = current//2


def heap_pop():         # heap에서 최소값 반환 및 삭제
    global heapcount
    result = heap[1]
    # 1. 마지막 요소를 root에 옮기기
    # 자식 중에서 큰 요소와 현재요소를 비교해서 자식요소가 더 작다면 교환
    heap[1] = heap[heapcount]
    heap[heapcount] = 0
    heapcount -= 1
    # 자식 요소중에서 작은 것 찾아야 함.
    parent = 1
    child = parent * 2 # 일단 왼쪽 잡기 오른쪽이 없을 수도 있으니
    if child + 1 <= heapcount: # True >> 오른쪽도 자식이 있다
        if heap[child+1] < heap[child]:
            child += 1
    # child : 이 위치에서는 자식들 중에서 더 작은 값을 가지는 자식의 번호
    while child <= heapcount and heap[child] < heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child]
        parent = child
        child = parent * 2
        if child + 1 <= heapcount: # 오른쪽 자식도 있다.
            if heap[child+1] < heap[child]:
                child += 1
    
    return result
