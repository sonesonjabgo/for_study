# 조건문 실습 문제
num = int(input('숫자를 입력하세요 : '))

if num%2 == 1:  # if num % 2:  >> 0 이 아닌 수는 truthy 값
    print('홀수')
else:           # 0 은 falsy
    print('짝수')

# 조건 표현식
value = '홀수' if num%2 else '짝수'
print(value)

