# 이진 검색
arr = [1,5,8,17,20,25,35,44] # 리스트가 정렬돼있어야 함
N = len(arr)

# key는 찾고자하는 값, 있으면 True, 없으면 False반환
def binary_search(key):
    start = 0
    end = N-1

    while True:
        if start > end:
            break
        # 1. 검색범위 중간값 찾기
        mid = (start + end)//2
        if arr[mid] == key:
            return True
        # 못찾은 경우, key가 mid보다 큰 경우 or key가 mid보다 작은 경우
        elif key > arr[mid]: # 더 큰 경우, 중간보다 인덱스가 작은건 볼 필요가 없음
            start = mid + 1  # 시작점을 중간 다음 인덱스로 설정
        else:  # key < arr[mid] # 더 작은 경우, 중간보다 인덱스가 큰 것은 볼 필요가 없음
            end = mid - 1 # 종료점을 중간 이전 인덱스로 설정
    return False

print(binary_search(17))
