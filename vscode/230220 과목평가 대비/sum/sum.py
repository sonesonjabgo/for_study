import sys
sys.stdin = open("input.txt", "r")

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_col = 0
    for i in range(100):
        sumcol = 0
        for j in range(100):
            sumcol += arr[i][j]
        if sumcol > max_col:
            max_col = sumcol

    max_row = 0
    for i in range(100):
        sumrow = 0
        for j in range(100):
            sumrow += arr[j][i]
        if sumrow > max_row:
            max_row = sumrow

    sum_dia1 = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                sum_dia1 += arr[i][j]

    sum_dia2 = 0
    for i in range(100):
        sum_dia2 += arr[99-i][i]

    maxnum = max_col
    for max in (max_col, max_row, sum_dia1, sum_dia2):
        if max > maxnum:
            maxnum = max
    print(f'#{tc} {maxnum}')
