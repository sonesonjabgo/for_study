arr = [5,6,1,4,3,7,8,2,9]
N = len(arr)
for i in range(N-1):
    min_idx = i
    for j in range(i+1, N):
        if arr[min_idx] > arr[j]:
            min_idx = j

    arr[min_idx], arr[i] = arr[i], arr[min_idx]
print(arr)

# 최솟값 찾아서 제일 앞에 있는 거랑 바꿔주는 방식
def choice(arr):
    N = len(arr)
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

arr = [5, 6, 1, 4, 3, 7, 8, 2, 9]
print(choice(arr))











