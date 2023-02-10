# 수확한 순서대로 당근 크기 기록
# 연속으로 크기 커지면 그 개수 알려줌
# 그 개수의 최대가 몇 인지

import sys
sys.stdin = open("carrotinput.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) # 당근의 개수
    C = list(map(int, input().split())) # 당근의 크기
    ans = cnt = 1 # 연속으로 커지지 않는 경우 구간의 최소 길이 1
    # 연속된 숫자가 나올 때 점수를 누적시킬 cnt
    # cnt의 최대값을 저장할 ans
    for i in range(N-1): # 마지막 당근은 비교할 대상이 없음
        if C[i] < C[i+1]:
            cnt += 1
            if ans < cnt:
                ans = cnt
        else:
            cnt = 1
    print(f'#{test_case} {ans}')

