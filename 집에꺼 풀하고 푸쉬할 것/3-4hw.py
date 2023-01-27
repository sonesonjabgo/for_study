s_triangle = input('삼각형의 각 변의 길이를 입력하시오. : ') # 3 3 3
a, b, c = s_triangle.split()
# 리스트 요소 하나씩 다른 변수에 저장하고 비교
# 비교하는 것을 반복해야 함
if a == b and b == c and c == a:
    print('정삼각형')
elif a == b or b == c or c == a:
    print('이등변삼각형')
elif (a**2 + b**2) == c**2 or (b**2 + c**2) == a**2 or (c**2 + a**2) == b**2:
    print('직각삼각형')
elif a + b > c or b + c > a or c + a > b:
    print('삼각형')
else:
    print('삼각형 아님')