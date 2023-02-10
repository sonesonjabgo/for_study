import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [''.join(input().split()) for _ in range(N)]
    # print(arr)
    # 연속된 1의 개수가 K개
    # 검사를 했을 때 1이라면 카운트를 하나 늘리고
    # 0 일 때 카운트 초기화
    # 카운트가 K라면 result + 1
    result = 0
    for i in range(N):
        count = ''
        max_count = K
        for j in range(N):
            if arr[i][j] == '1':
                count += '1'
                if j == N-1:
                    if len(count) == K:
                        result += 1
            elif arr[i][j] == '0':
                if len(count) == K:
                    result += 1
                count = ''
########################################################
    for i in range(N):
        count = ''
        max_count = K
        for j in range(N):
            if arr[j][i] == '1':
                count += '1'
                if j == N-1:
                    if len(count) == K:
                        result += 1
            elif arr[j][i] == '0':
                if len(count) == K:
                    result += 1
                count = ''
    print(f'#{test_case} {result}')