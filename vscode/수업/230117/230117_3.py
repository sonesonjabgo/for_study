# List Comprehension
# 1 ~ 3의 세제곱의 결과가 담긴 리스트를 만드시오
cubic_list = []
for number in range(1, 4):
    cubic_list.append(number ** 3)
print(cubic_list)

# [1, 8, 27]

cubic_list = [number ** 3 for number in range(1,4)]
print(cubic_list)

# [1, 8, 27]