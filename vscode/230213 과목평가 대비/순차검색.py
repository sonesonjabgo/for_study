# 말 그대로 순차적으로 검색하는 것
# 처음부터 찾을 때 까지 전부 대조해서 찾는 것

# 정렬됐을 때와 정렬되지 않았을 때로 다르게 해야 한다
# 정렬되지 않았을 때는
# 정말 찾을 때까지 해야하고

# 정렬됐을 때는 찾으려는 숫자보다 대조한 숫자가 클 때
# 더 이상 검색을 안해도 된다 (존재 X)

# 정렬되지 않은 경우
arr = [10, 1, 6, 8, 2, 9, 3, 4]
N = len(arr)
i = 0 # 인덱스
f = 9 # 찾으려는 숫자
while i < N and arr[i] != f:
# 인덱스가 범위를 넘어가지 않고 찾는 숫자를 찾을 때 까지
    i += 1
if i < N:
    print(i)
# i가 N을 넘어가지 않았는데 반복문이 끝났다면 f를 찾았다는 것
else:
    print('없다')

###############################################
# 정렬된 경우
# 위의 arr를 버블정렬로 정렬해보자
for i in range(N-1, 0, -1):
    for j in range(0, i):
       if arr[j] > arr[j+1]:
           arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)
i = 0
while i < N and arr[i] < f:
    i += 1
if i < N and arr[i] == f:
    print(i)
else:
    print('없다')


def sequence(arr, key):
    N = len(arr)
    for i in range(N):
        if arr[i] == key:
            return i

def sort_sequence(arr, key):
    N = len(arr)
    i = 0
    while i < N and arr[i] < key:
        i += 1
    if i < N and arr[i] == key:
        return i
    else:
        return '없다'

arr = [10, 1, 6, 8, 2, 9, 3, 4]
print(sequence(arr, 9))

arr2 = [1,2,3,4,5,6]
print(sort_sequence(arr, 7))




