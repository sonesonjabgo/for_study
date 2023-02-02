# 버스는 0번에서 출발
# 한번 충전으로 이동할 수 있는 정류장 수 K
# 종점은 N
# 충전기가 설치된 정류장 M
# 1 <= K, N, M <= 100
# 테스트 케이스 T
# 3
# 3 10 5
# 1 3 5 7 9
T = int(input()) # 3

for t in range(T):
    K, N, M = map(int, input().split())  # 3 10 5
    busstopnum = list(map(int, input().split()))  # [1 3 5 7 9]
    charge = 0
    mynum = K
    for n in range(N): # 1 2 3 4 5 6 7 8 9
        if n in busstopnum:
            for num in range(M-1): # 0 1 2 3
                if mynum - (busstopnum[num+1] - busstopnum[num]) < 0: # 남은 이동 거리 - 다음 충전기까지의 거리
                    charge += 1
                    mynum = K
        print(n, mynum)
        mynum -= 1
    # if mynum < 0:
    #     charge = 0

    print(f'답은 {mynum} {charge}')


