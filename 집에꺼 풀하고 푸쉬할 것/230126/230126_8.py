# 재귀로 카피하는 방법
# 리스트를 인자로 받아서 복사하여 리스트를 반환하는 함수
def my_deep_copy(target):
    target_copy = []
    for e in target:
        if type(e) == int or type(e) == str:
            target_copy.append(e)
        elif type(e) == list:
            copied_list = my_deep_copy(e)
            target_copy.append(copied_list)
   # 요소가 숫자나 문자열일 경우 > 그냥 복사
   # 요소가 리스트일 경우 >> 이것도 복사해야 함
    return target_copy

arr = [1,2,[10,20,30,[1000,2000,3000]],5,[100,200,300]]
arr_copy1 = arr[:]
arr_copy2 = my_deep_copy(arr)
arr[2][1] = -10
print('원본')
print(arr)
print('----------------')
print('복사본 (얕은 복사)')
print(arr_copy1)
print('----------------')
print('복사본 (깊은 복사)')
print(arr_copy2)

# 슬라이싱으로 복사하게 되면 리스트는 주소를 복사해서 같은 리스트를 가리키게 돼서 
# arr의 값을 바꿨을 때 같이 가리키는 리스트의 값이 변경이 된다

# 위의 재귀를 이용한 깊은 복사를 하게 되면
# 리스트의 주소를 복사하는 것이 아니라
# 리스트 자체를 복사하기 때문에 값이 변경되지 않는다
# 당연히 주소도 다르다.