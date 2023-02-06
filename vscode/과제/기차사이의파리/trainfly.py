import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = list(map(int, input().split()))
    dis = N[0] / (N[1] + N[2])
    rst = dis * N[3]

    print(f'#{t} {rst}')