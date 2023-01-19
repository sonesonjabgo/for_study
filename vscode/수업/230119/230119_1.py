# map 활용
# def my_magic_func(n):
#     return n * 10

# my_list = [1, 2, 3, 4, 5]

# rlt = map(my_magic_func, my_list)
# print(rlt)  # <map object at 0x0000020F0D99DF40> 
#             # map함수는 map 오브젝트를 넘겨줌
# print(list(rlt)) # 리스트로 형변환하면 잘 보임

# zip 활용
name_list = ['신동민', '서재현', '박영서', '이태성', '정예원', '이은석']
age_list = [17, 18, 22, 24, 25, 19]

for each in zip(name_list, age_list):
    print(each)
# ('신동민', 17)
# ('서재현', 18)
# ('박영서', 22)
# ('이태성', 24)
# ('정예원', 25)
# ('이은석', 19)

for name, age in zip(name_list, age_list):
    print(name, age)
# 이런 식으로 따로 받을 수 있다.