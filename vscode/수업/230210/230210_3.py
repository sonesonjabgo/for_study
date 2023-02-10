# 숫자 배열 회전
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() + [0] for _ in range(N)]
    a1 = [[0]*N for _ in range(N)]  # 90도
    a2 = [[0]*N for _ in range(N)]
    a3 = [[0]*N for _ in range(N)]


    # 회전각도에 따른 위치값을 저장
    for i in range(N):
        for j in range(N):
            a1[i][j] = arr[N-1-j][i]
            a2[i][j] = arr[N-1-i][N-1-j]
            a3[i][j] = arr[j][N-1-i]
    for a, b, c in zip(a1,a2,a3):
        print(f'{''.join(a)}, {''.join(b)}, {''.join(c)}')

#############################################################
    # arr_t = list(map(list,zip(*arr)))
    #
    # for i in range(N):
        print(f'{''.join(arr_t[i][::-1])} {''.join(arr[N-1-i][::-1])} {''.join(arr_t[N-1-i])}')