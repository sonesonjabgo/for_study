# arr = ['a', 'b', 'c', 'd', 'e']
# N = 5
# for i in range(1<<N):
#     for j in range(N):
#         if i & (1<<j) != 0:
#             print(arr[j], end=' ')
#     print()

arr = [x for x in range(1, 10)]
N = len(arr)
for i in range(1, 1<<N): # 2**N 0000000000
    count = 0
    for j in range(N):
        if i & (1<<j) != 0:
            count += arr[j]
    if count == 0:
        print(True)
