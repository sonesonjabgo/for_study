# 1945 간단한 소인수분해

# N = 50 = 2 * 5 * 5
# 5가 두개인지 아는 건 반복해서
# 반복 >> cnt
# if N%5 == 0
#   cnt

import sys
sys.stdin = open("input.txt", "r")

divs = [2, 3, 5, 7, 11]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    cnts = [0] * len(divs)

    for i in range(len(divs)):
        while N%divs[i] == 0:
            cnts[i] += 1
            N=N//divs[i]
