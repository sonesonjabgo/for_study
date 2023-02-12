# 오른쪽에 있는 원소와 비교하여 더 크면 자리를 바꿔가면서
# 오름차순으로 정렬되는 것
# 숫자를 일일히 대조해서 옮기는 것이기 때문에
# 집합에 많은 숫자가 있을 때는 느리다. O(n**2)

# arr = [55, 7, 78, 12, 42]
# for i in range(len(arr)-1 , 0, -1):
# # i를 뒤에서부터 시작하는 이유는
# # 최댓값을 제일 뒤에 정렬시키기 위함임
# # 그렇다는 건 제일 뒤부터 값을 정렬시킨다라는 뜻
#     for j in range(0, i):
#     # 0부터 i라는 것은 i는 처음 제일 뒤 인덱스가 되고
#     # 하나씩 채울 수록 뒤에서 하나 씩 앞으로 댕겨지면서
#     # 이미 그 중 가장 큰 수로 채워진 뒤쪽 숫자들은 확인할 필요가
#     # 없기 때문이다.
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)

######################################################





arr = [59, 60, 12, 88, 3, 4, 1, 77]
for i in range(len(arr)-1, 0, -1):
# arr의 길이 -1 은 정렬된 리스트의 마지막
# 즉, 최대값이 들어갈 자리를 말함
# 0번 인덱스는 어차피 최솟값이 남아있으니 검색할 필요 없음
    for j in range(0, i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)


# 해당 인덱스와 다음 인덱스를 비교해서 큰 수를 뒤쪽에 넘기고
# 최댓값을 뒤부터 채우는 방식

def bubble(arr, n):
    for i in range(n-1, 0, -1):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [27, 18, 99, 12, 3, 6, 34, 7]
N = len(arr) # 8
print(bubble(arr, N))







