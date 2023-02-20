import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_fly = 0
    for k in range(N-M+1):
        for l in range(N-M+1):
            fly = 0
            for i in range(M):
                for j in range(M):
                    fly += arr[k+i][l+j]
            if fly > max_fly:
                max_fly = fly

    print(f'#{tc} {max_fly}')