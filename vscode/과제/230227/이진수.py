def Bbit_print(n):
    output = ''
    for j in range(3, -1, -1):
        output += '1' if n & (1 << j) else '0'
    print(output, end='')




T = int(input())
for tc in range(1, T+1):
    N, data = input().split()
    data = list(data)
    numdict = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    print(f'#{tc} ', end='')
    for i in data:
        if i in numdict:
            i = numdict[i]
        else:
            i = int(i)
        # print(f'{i} =', end=' ')

        Bbit_print(i)
    print()