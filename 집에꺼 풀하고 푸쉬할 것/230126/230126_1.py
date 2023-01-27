sample_list = [11, 22, 33, 55, 66]

# 주어진 리스트의 3번 index에 있는 항목을 제거하고 변수에 할당해 주세요.

popnum = sample_list.pop(3)
print(sample_list, popnum)

# sample_list의 가장 뒤에 를 추가해보세요
sample_list.append(77)
print(sample_list)

# 할당해놓은 변수의 값을 sample_list 2번 index에 추가해 보세요
sample_list.insert(2, popnum)
print(sample_list)