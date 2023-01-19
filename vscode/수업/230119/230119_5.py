# 패킹 / 언패킹

# x, y = 1, 2
# z = 1, 2, 3

# a, b = 1, 2, 3, 4 # too many values to unpack 에러
# 이럴 때 * 를 사용

# a, *b = 1, 2, 3, 4 # a에 1을 넣고 나머지는 묶어서 b에 넣어라
# print(a, b)

# def my_sum(a, b, c):
#     return a + b + c

# num_list = [10, 20, 30]

# rlt1 = my_sum(num_list[0], num_list[1], num_list[2]) # 번거롭다
# rlt2 = my_sum(*num_list) # 각 자리에 들어감 간단
# print(rlt1, rlt2)

# # 매개변수에 패킹을 넣는 경우
# def test(*values):
#     for value in values:
#         print(value)

# test(1)
# test(1, 2)
# test(1,2,3,4)

def my_sum(a, *args):
    rlt = 0
    for value in args:
        rlt += value
    return rlt

print(my_sum(1,2,3))  # 1은 a에 들어가고 2,3은 args에 묶여서 들어감