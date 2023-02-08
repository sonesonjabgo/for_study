# 출력 예시 
#  25

def sum_of_repeat_number(list):
    result = 0
    for num in list:
        if list.count(num) == 1:
            result += num
    print(result)

num_list = [4, 4, 7, 8, 10, 4]
sum_of_repeat_number(num_list)