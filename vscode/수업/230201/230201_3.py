# swea min max
T = int(input()) # 한 줄 입력받아서 숫자로 변경
# 첫 줄에는 N
# 두 번째 줄에는 N개의 양의 정수
for tc in range(T):
    N = int(input())
    # 문자열 > 문자열 리스트 > 각 요소를 숫자로 변경
    # '10 13 23 45 789'
    # ['10', '13', '23', '45', '789']
    # [10, 13, 23, 45, 789]
    # map(func, iterable) : iterable의 각 요소에 func 적용
    # map이 iterable을 반환해주긴 하는데 index 적용이 가능한 형태로 바꿔야함
    numbers = list(map(int, input().split()))
    #####################
    # N과 numbers를 이용해서 각 테스트케이스의 정답 출력
