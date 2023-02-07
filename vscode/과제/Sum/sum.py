import sys
sys.stdin = open("input (1).txt", "r")

for _ in range(10):
    T = int(input())
    my_list = []
    maxrow = 0
    maxinx = 0

    for _ in range(100):
        num_list = list(map(int, input().split()))
        my_list.append(num_list)

    for i in range(100):
        sumrow = 0
        for j in range(100):
            sumrow += my_list[i][j]
        if sumrow >= maxrow:
            maxrow = sumrow


    for j in range(100):
        suminx = 0
        for i in range(100):
            suminx += my_list[i][j]
        if suminx >= maxinx:
            maxinx = suminx

    sumdia1 = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                sumdia1 += my_list[i][j]

    sumdia2 = 0
    for i in range(100):
        for j in range(100):
            if i + j == 99:
                sumdia2 += my_list[i][j]

    result = [maxrow, maxinx, sumdia1, sumdia2]
    resultmax = 0
    for i in result:
        if i >= resultmax:
            resultmax = i

    print(f'#{T} {resultmax}')