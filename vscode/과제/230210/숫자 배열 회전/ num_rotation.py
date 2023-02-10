import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    a1 = [[0]*N for _ in range(N)] # 90도
    a2 = [[0]*N for _ in range(N)] # 180도
    a3 = [[0]*N for _ in range(N)] # 270도
    # arr의 한 글자씩 찾아서 a1,a2,a3에 넣어 줄 것임.

    for i in range(N):
        for j in range(N):
            a1[i][j] = arr[(N-1)-j][i]
            a2[i][j] = arr[(N-1)-i][(N-1)-j]
            a3[i][j] = arr[j][(N-1)-i]
    print(f'#{test_case}')
    for a, b, c in zip(a1, a2, a3):
        print(''.join(a), ''.join(b), ''.join(c))