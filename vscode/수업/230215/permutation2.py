arr = [
    ['01','02','03','04','05'],
    ['11','12','13','14','15'],
    ['21','22','23','24','25'],
    ['31','32','33','34','35'],
    ['41','42','43','44','45']
]

N = len(arr)
perm_arr = [0] * N
# idx번째에 넣을 수 있는 숫자 다 넣기
# used = [[0] * N for _ in range(N)]
used = [0] * N
# def perm(idx):
#     if idx == N: # N 번째 행에 도달하면 최솟값 구하는 코드 아래 들어가면 됨
#         print(perm_arr)
#         return
#     for i in range(N):
#         for j in range(N):
#             if not used[i][j]:
#                 perm_arr[idx] = arr[i][j]
#                 for k in range(N):
#                     used[i][k] = 1
#                     used[k][j] = 1
#                 perm(idx+1)
#                 for k in range(N):
#                     used[i][k] = 0
#                     used[k][j] = 0

def perm(idx):
    if idx == N:
        print(perm_arr)
        return
    for i in range(N):
        if not used[i]:
            perm_arr[idx] = arr[i]
            used[i] = 1
            perm(idx+1)
            used[i] = 0

perm(0)