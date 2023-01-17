# 명시적인 형변환 int(), float(), str()
# 정수형 문자형 정수로 바꾸기
a =  int('123')
print(type(a))

s = str(123.65)
print([s])


# 각 자리 수 합
str_num = '12345'
# 각 자리 수 자르기, 각 자리 수 문자를 숫자로 변경, 모든 숫자의 합
# map(int,시퀀스) > 문자열을 하나하나 다 숫자형으로 바꿔버림 
print(list(map(int,str_num)))
print(sum(list(map(int,str_num))))