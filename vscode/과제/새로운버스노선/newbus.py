import sys
sys.stdin = open("sample_in.txt", "r")

T = int(input()) # 테스트 케이스 수
for t in range(1, T+1):
    N = int(input()) # 버스 대 수
    cnt = [0] * 1001 # 1000개의 정류장
    # 노선이 정류장에 들린다면 해당 노선의 cnt[idx]에 1을 더해준다.
    for n in range(N): # N 만큼 버스노선에 대한 정보가 들어온다.
        info = list(map(int, input().split()))
        if info[0] == 1:
            route = [n for n in range(info[1], info[2]+1)]
            for stop in route:
                cnt[stop] += 1
        elif info[0] == 2:
            if info[1] % 2: # 홀수면
                route = [n for n in range(info[1], info[2] + 1) if n % 2]
            else:
                route = [n for n in range(info[1], info[2] + 1, 2)]
            for stop in route:
                cnt[stop] += 1
        elif info[0] == 3:
            if info[1] % 2: # 홀수면
                route = [n for n in range(info[1], info[2] + 1) if n % 3 == False and n % 10]
            else:
                route = [n for n in range(info[1], info[2] + 1, 2) if n % 4 == False]
            for stop in route:
                cnt[stop] += 1

    maxnum = 0
    for i in range(len(cnt)):  # 0 1 2 3 4 5 6 7 8 9
        if cnt[i] >= maxnum:
            maxnum = cnt[i]

    print(f'#{t} {maxnum}')