# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이
# int요소를 가진 리스트로 만들고
# 크기 순으로 정렬한 뒤
# 앞에서 개, 뒤에서 3개 각각 더한 것을 뺀 값을 반환

# 일단 T는 테스트 케이스의 개수
T = int(input())
for t in range(1, T+1): # 3이 들어가면 1 2 3
    # 그 뒤에 요소의 개수 N 부분합할 개수 M
    # numbers는 배열이 될 수들
    M, N = map(int, input().split()) # 10 3
    numbers = list(map(int, input().split())) # 1 2 3 4 5 6 7 8 9 10
    maxnum = 0
    minnum = 10000 * N  # 정수의 범위가 1 <= num <= 10000
    for m in range(0, M-(N-1)): # 0 1 2 3 4 5 6 7 8 9
        # 6262 6004 1801 7660 7919 1280 525 9798 5134 1821
        # 앞에서 N만큼인 숫자 뒤에서 N만큼의 숫자
        sumnum = 0
        for number in range(m, N+m):
            sumnum += numbers[number]

        if sumnum > maxnum:
            maxnum = sumnum

        if sumnum < minnum:
            minnum = sumnum

    print(f'#{t} {maxnum - minnum}')
