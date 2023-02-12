# 이진 검색은 숫자가 정렬되어 있어야 한다.
# 찾으려는 숫자 리스트의 중앙값보다 크거나 작을 때
# 범위를 축소시켜 값을 찾는 방식

arr = [1, 5, 4, 2, 7, 4, 8]
# 숫자를 정렬 먼저..
# 카운팅 정렬을 써보자
N = len(arr)
k = 8
counts = [0] * (k+1)
sort = [0] * N

for i in range(N):
    counts[arr[i]] += 1

for i in range(1, len(counts)):
    counts[i] = counts[i-1] + counts[i]

for i in range(N-1, -1, -1):
    counts[arr[i]] -= 1
    sort[counts[arr[i]]] = arr[i]
# print(sort)
f = 5
# start 와 end를 둬서
# f의 위치에 따라
# start 와 end를 다른 값으로 선언해주어서
# 검색의 범위를 줄인다
start = 0
end = N-1
while start <= end:
    middle = (start + end) // 2
    # 중간값 인덱스 구하기
    if sort[middle] == f:
        print(middle)
        break
    elif sort[middle] > f:
        end = middle - 1
    else:
        start = middle + 1


def binary(arr, key):
    N = len(arr)
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == key:
            return middle
        elif arr[middle] > key:
            end = middle -1
        else:
            start = middle +1
    if start > end:
        return False

arr = [1, 2, 4, 4, 5, 7, 8]
key = 3
print(binary(arr, key))

