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
    empty = [0] * 10
    for i in busstopnum:
        empty[i] = 1     # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    charge = 0
    idx = 0
    left = K
    # print(busstopnum[-1])
    for n in range(len(N)):
        if idx >= N:
            break
        # left를 하나 소비시키고 idx에 하나 추가시킬 것임
        left -= 1  # 2
        idx += 1  # 1
        if empty[idx] == 1: # idx가 충전소의 위치에 왔을 때
            if left - (busstopnum[1] - busstopnum[0]) < 0: # 충전을 할지 안할지의 여부가 들어가야 함



