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

while True:
    year = int(input('몇 년도 입니까? : '))
    if cal.isleap(year):
        print('윤년입니다. 연도를 다시 입력해주세요.')
        
    else:
        # 여기에 캘린더 출력이 들어가야 함
        print(cal.calendar(year))
        break

# 월 입력
# 일 입력
# 몇월 몇일이 월요일인지 파악 (캘린더 모듈 활용)
# 월요일이면 > 경고문 출력
month = int(input('월 입력 : '))
day = int(input('일 입력 : '))
weekday = cal.weekday(year, month, day)
if weekday == 0:
    print('경고 월요일입니다.')
# 입력받은 연,월,일 딕셔너리에 넣어서 출력
weekday_dict = {0:'월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}
my_dict = {'년': year, '월': month, '일': day, '요일': weekday_dict[weekday]}
print(my_dict)
