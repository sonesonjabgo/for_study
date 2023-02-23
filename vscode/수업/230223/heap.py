# 최대 100개의 key
# 최대힙

def enq(n):
    global last
    last += 1           # 완전이진트리에 마지막 정점을 추가하고
    heap[last] = n      # 마지막 정점에 저장
    c = last            # 부모가 있고, 부모 > 자식 조건 검사를 위해
    p = c//2
    while p>0 and heap[p]<heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p           # 옮긴 자리에서 부모와 비교하기 위해
        p = c // 2 
    return





heap = [0] * 101        # 완전이진트리 1번 - 100번 인덱스 준비
last = 0                # 완전이진트리의 마지막 정점 번호
print(heap)
enq(5)
print(heap)
enq(15)
enq(8)
enq(20)
print(heap)
