word1 = input('첫 번째 이름을 입력하세요 : ')
word2 = input('두 번째 이름을 입력하세요 : ')

ordword1 = list(map(ord, word1)) 
ordword2 = list(map(ord, word2))

# print(ordword1, type(ordword1)) 
# [97, 112, 112, 108, 101] <class 'list'>

# word1 과 word2를 비교해서 더 높은 숫자를 반환하는 코드 필요
number1 = sum(ordword1)
number2 = sum(ordword2)

# print(number1, number2)
if number1 > number2:
    print(word1)
elif number2 > number1:
    print(word2)
else:
    print('두 문자열의 아스키 코드 합이 같습니다.')