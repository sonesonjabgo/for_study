# 아래의 함수를 lambda함수로 만들어보기
def my_magic_func(n):
    return n * 10


map_obj = map(my_magic_func, [1, 2, 3])
rlt = list(map_obj)

print(rlt)

map_obj2 = map(lambda x: x * 10, [1,2,3])
rlt2 = list(map_obj2)

print(rlt2)
# [10, 20, 30]
# [10, 20, 30]