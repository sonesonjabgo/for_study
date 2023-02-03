import sys
sys.stdin = open("input1.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) # 수열의 길이
    arr = list(map(int, input())) # 0과 1로 구성된 수열

    ans = 0
    cnt = 0
    for i in range(N):
        if arr[i] == 0:
            cnt = 0
        else: # arr[i] 값은 0 아니면 1
            cnt += 1
            # cnt의 최대값을 저장해야 함
            if ans<cnt:
                ans = cnt
    print(f'#{test_case} {ans}')

