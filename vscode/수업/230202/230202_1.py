# # 거품 정렬
arr = [5, 6, 1, 3, 4, 7, 9, 8, 2]
N = 9
# # 두 개 비교해서 뒤로 보내기
# for _ in range(N-1):
#     for i in range(0, N-1):
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i] # 쉼표로 구분 > 튜플
#             # 튜플로 묶여 있는 것을 언패킹 하는 과정임
#             # 이 과정을 끝까지 다 했을 때 arr의 제일 큰 숫자가 제일 뒤 (N-1)로 감
#
for j in range(N-1):
    for i in range(0, N-1-j): # 한번 돌 때마다 마지막에 제일 큰 숫자가 들어가기 때문에
        # 굳이 마지막까지 매번 비교할 필요가 없음
        # 필요없는 반복을 줄인 것
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
#

# # 선택 정렬
# arr = [5, 6, 1, 3, 4, 7, 9, 8, 2]
# # 제일 작은 애 선택해서 자리에 넣어주기
# # 제일 작은 애 위치 찾기
# min_idx = 0 # 일단 제일 앞 숫자를 작은 수라고 가정
# for i in range(N):
#     # 내가 알고 있는 제일 작은 수보다 더 작으면 >> 걔가 제일 작은 수
#     if arr[i] < arr[min_idx]:
#         min_idx = i
# # 제일 작은 애의 위치 min_idx
# arr[0], arr[min_idx] = arr[min_idx], arr[0]
# # 위의 작업은 0번에 들어갈 애를 찾은 과정임
#
# # 1번을 바꿀 것이다
# min_idx = 1 # 일단 제일 앞 숫자를 작은 수라고 가정
# for i in range(0, N):
#     # 내가 알고 있는 제이 작은 수보다 더 작으면 >> 걔가 제일 작은 수
#     if arr[i] < arr[min_idx]:
#         min_idx = i
# # 제일 작은 애의 위치 min_idx
# arr[1], arr[min_idx] = arr[min_idx], arr[1]

# 0번부터 N-2번까지 위치에 들어갈 작은 숫자 찾기
# 맨 뒷자리 N-1번은 어차피 제일 큰 숫자가 남아서 들어가있음
arr = [5, 6, 1, 3, 4, 7, 9, 8, 2]
for j in range(0, N-1): # 각 위치를 의미
    # -1 이유는 마지막에 들어갈 숫자는 어차피 남아있는 제일 큰 숫자
    min_idx = j  # 일단 해당 인덱스에 들어갈 숫자를 가장 작은 수라고 가정
    for i in range(j, N):
        # 내가 알고 있는 제일 작은 수보다 더 작으면 >> 걔가 제일 작은 수
        if arr[i] < arr[min_idx]:
            min_idx = i
    # 제일 작은 애의 위치 min_idx
    arr[j], arr[min_idx] = arr[min_idx], arr[j]
    print(arr)