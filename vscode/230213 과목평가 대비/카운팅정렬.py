# # 카운팅 정렬은 집합 내의 가장 큰 숫자를 알아야 한다
# # 각 원소마다 개수를 카운트한 숫자를 적어놓을 공간을 만들어야 하기 때문
# # 때문에 최대값의 간격이 큰 경우에는 별로 효과적이지 않다.
# # O(n+k)
# arr = [0, 4, 1, 3, 1, 2, 4, 1]
# k = 4 # 최댓값
# count = [0] * (k+1) # 해당하는 인덱스에 1을 올릴 빈 리스트를 만듦
# for i in range(len(arr)):
#     count[arr[i]] += 1
# # count에 arr가 갖고있는 숫자가 올라간다.
# # print(count)
# # [1, 3, 1, 1, 2]
# # count를 다음 인덱스에 누적시켜야 함
# # [1, 4, 5, 6, 8]
# for i in range(1, len(count)):
#     count[i] = count[i-1] + count[i]
# # print(count)
# # 이제 원래 집합의 끝 값부터 정렬해준다.
# # 끝 값은 1인데 count의 1은 4이다
# # 이 의미는 1를 포함한 1보다 작은 수는 총 4개라는 것이다.
# # 그래서 1은 적어도 정렬된 수 중에 4번째(temp[3])에 들어가도 된다는 것
# # 그리고 해당 인덱스의 count를 1감소 시킨다
# # 이것은 다음번 검사에서 위에서 적었던 것 처럼 작용한다
# # 1이 다시 들어올 경우 1을 포함한 작은 숫자가 3개가 되는 것이여서
# # 1이 3번째에 들어가도 된다는 것.
# sort = [0] * len(arr)
# # 정렬해서 값을 넣을 리스트
# for i in range(len(arr)-1, -1, -1):
#     count[arr[i]] = count[arr[i]] - 1
#     # i는 7 arr[7] = 1 count[1]이 1감소됨
#     sort[count[arr[i]]] = arr[i]
# print(sort)
#
# #######################################################
#
# # 카운팅정렬은 입력된 리스트의 최댓값이랑
# # 값들의 갯수를 저장할 리스트랑
# # 정렬한 값을 저장할 리스트가 필요하다

arr = [15, 1, 1, 3, 0, 3, 4, 2, 9, 11, 10, 4]
k = 15 # arr의 최댓값
N = len(arr)
counts = [0] * (k+1) # 해당 인덱스에 맞는 값이 들어가야 하기에 +1
sort = [0] * N

# 처음 arr의 각 요소들의 개수를 세서 count에 저장해야 함
for i in range(N):
    count = 0
    for j in range(N):
        if arr[i] == arr[j]:
            count += 1
    counts[arr[i]] = count
# print(counts)
# 그리고 counts의 값들을 뒤로 누적시킴
for i in range(1, len(counts)):
    counts[i] = counts[i-1] + counts[i]

# 원래 리스트 뒤부터 검사하면서 counts의 해당 인덱스 값 1씩 빼주고
# 그 값을 sort의 인덱스로 원래 리스트의 숫자 넣어줌
for i in range(N-1, -1, -1):
    counts[arr[i]] -= 1 # 2 - 1
    sort[counts[arr[i]]] = arr[i]

print(sort)


def counting(arr, K):
    N = len(arr)
    counts = [0] * (K+1)
    sort = [0] * N

    # 카운트
    for i in range(N):
        counts[arr[i]] += 1 # arr[0] = 15 > counts[15] += 1

    # 누적
    for i in range(1, len(counts)):
        counts[i] = counts[i-1] + counts[i]

    # 정렬
    for i in range(N-1, -1, -1):
        counts[arr[i]] -= 1 # counts[15] -= 1
        # -1 했을 때 14가 남아 있으면 14인덱스로 들가면 됨
        sort[counts[arr[i]]] = arr[i]

    return sort

arr = [15, 1, 1, 3, 0, 3, 4, 2, 9, 11, 10, 4]
K = 15
print(counting(arr, K))





