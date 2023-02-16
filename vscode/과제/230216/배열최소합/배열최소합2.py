#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    sol_arr = [0] * N

    def solve(idx):
        for i in range(N):
            if idx == N:
                print(sol_arr)
                return
            if not used[i]:
                sol_arr[idx] = i # arr[idx][i]가 해당 값이라는 것
                used[i] = 1
                solve(idx+1)
                used[i] = 0
    solve(0)