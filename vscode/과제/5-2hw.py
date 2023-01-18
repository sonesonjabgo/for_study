# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}

# 연도 입력
# 연도가 윤년인지 계산 > 이것도 캘린더로 가능
# calendar.isleap(year)
# 윤년이면 > 윤년 출력문 + 연도 입력 재진행
# 아니면 캘린더 출력 (캘린더 모듈 활용)
import calendar as cal
print(cal.isleap(2016))

while True:
    year = int(input('몇 년도 입니까? : '))
    if cal.isleap(year):
        print('윤년입니다. 연도를 다시 입력해주세요.')
        continue
    else:
        # 여기에 캘린더 출력이 들어가야 함
        print(cal.prcal(year))
        break

# 월 입력
# 일 입력
# 몇월 몇일이 월요일인지 파악 (캘린더 모듈 활용)
# 월요일이면 > 경고문 출력
month = input()
# 입력받은 연,월,일 딕셔너리에 넣어서 출력


