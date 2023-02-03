# 6485 삼성시 버스노선
# 삼성시에 있는 5,000개의 버스 정류장은 관리의 편의를 위해 1에서 5,000까지 번호가 붙어 있다.
# 그리고 버스 노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고,
# Bi이하인 모든 정류장만을 다니는 버스 노선이다.
# P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램을 작성하라.

# 빈도 수 배열
# 1. cnts [] 빈도수 표시 (n개)
# 2. 지정된 정류장 버스 개수

import sys
sys. stdin = open('s_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # [1] N번 반복하면서 노선입력, 빈도수 표시
    cnts = [0]*5001
    for _ in range(N):
        S, E = map(int, input().split())
        for i in range(S, E+1):
            cnts[i] += 1

    P = int(input())
    alst = []
    for _ in range(P):
        p = int(input())
        alst.append(cnts[p])

    print(f'#{test_case}, '*alst)