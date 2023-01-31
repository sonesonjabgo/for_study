def sum_of_digit(num):
    strnum = list(str(num))
    strnum = map(int, strnum)
    result = sum(strnum)
    print(result)

def usefor(num):
    result = 0
    strnum = str(num)
    for num in strnum:
        result += int(num)
    print(result)

sum_of_digit(3904) # 16
usefor(3904)