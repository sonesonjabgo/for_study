# partition : 기준을 잡고 작은 값과 큰 값으로 구분
# 퀵 정렬 : 나뉘어진 작은 값들과 큰 값들을 각각 같은 작업을 반복
arr = [6,2,3,5,1,7,6,9,8,4,2,3]
def partition(start, end):
    pivot = arr[start]
    # 임의의 값 x를 잡아서, x보다 큰 값과 작은 값으로 나누어 주기
    i = start
    j = end
    while i <= j:
        # i는 1씩 증가하면서 pivot보다 큰 값 찾기
        # j는 1씩 감소하면서 pivot보다 작은 값 찾기
        while i <= j and arr[i] <= pivot: # i <= j의 의미는 값이 역전된 순간 어차피 자리를 바꾸는 것이 의미가 없기 때문이다.
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        # 찾으면 교환하는데 단, i가 j보다 작을 때만
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # 교환이 끝났으면 pivot 자리 잡아주기
    arr[start], arr[j] = arr[j], arr[start]
    # pivot의 위치를 반환
    return j

def quick_sort(start, end):
    # 만약에 정렬하려는 구간의 길이가 1이라면 아무작업도 안함
    if start >= end:
        return
    # partition을 수행
    pivot = partition(start, end)
    # 수행 결과로 나온 pivot을 기준으로
    # 왼쪽과 오른쪽 부분을 별도로 각각 정렬 수행
    quick_sort(start, pivot-1)
    quick_sort(pivot+1, end)

N = len(arr)
quick_sort(0, N-1)
print(arr)