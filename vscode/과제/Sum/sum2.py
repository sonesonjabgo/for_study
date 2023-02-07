# 교수님이 수업 때 하신 것
T = 10
for _ in range(T):
    tc = int(input())
    result = -0xffffffff
    # 각 행의 합은 integer 범위를 넘어가지 않는다.
    # 라는 조건이 있기 때문에 위의 코드 사용 가능
    board = [list(map(int, input().split())) for _ in range(100)]
    # 100*100 행렬 입력받아서 리스트로 만들기

    # 행의 합
    for i in range(100):        # 가로줄 이동
        sum_row = 0
        for j in range(100):    # 한 행 순회
            sum_row += board[i][j]
        if sum_row > result:
            result = sum_row

    # 열의 합
    for i in range(100):        # 세로줄(열) 이동
        sum_col = 0
        # 행 이동
        for j in range(100):    # 한 열 순회
            sum_col += board[j][i]
        if sum_col > result:
            result = sum_col

    sum_dia1 = 0 # 같을 때
    sum_dia2 = 0 # 더해서 99 나올 때
    for i in range(100):
        for j in range(100):
            if i == j:
                sum_dia1 += board[i][j]
            if i + j == 99:
                sum_dia2 += board[i][j]

    max_v = result
    for e in (sum_dia1, sum_dia2):
        if e > result:
            result = 0


    print(f'#{tc} {result}')