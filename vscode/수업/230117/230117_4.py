# Dictionary Comprehension 실습
cubic_dict = {}

for number in range(1, 4):
    cubic_dict[number] = number ** 3

print(cubic_dict)
# {1: 1, 2: 8, 3: 27}


cubic_dict = {number: number ** 3 for number in range(1, 4)}
print(cubic_dict)
# {1: 1, 2: 8, 3: 27}