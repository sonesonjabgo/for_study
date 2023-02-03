# elec bus 전기버스
# 다음 충전 정류장까지 충전 안하고 올 수 있나?
# 못오면 이전에서 충전
T = int(input())
for tc in range(1, T+1):
    count = 0
    K, N, M = map(int, input().split())
    # 충전기가 설치되어 있는 정류장 리스트 받기
    stops = list(map(int, input().split()))
    stops.append(N)
    stops.insert(0,0)

    # 이전에 충전한 위치 기억, 해당 정류장까지
    # 충전 안하고 올 수 있으면, 다음 정류장으로
    # 충전 안하고 못오면, 이전 정류장에서 충전
    position = 0  # 이전에 내가 충전한 정류장 번호 저장할 변수
    for i in range(M+2): # 충전소 있는 정류장 개수 + (0번째 ,마지막 도달 10 정류장)
        if stops[i] - stops[i-1] > K: # 불가능한 경우
            # 정류장끼리의 거리 > K
            # 다음 정류장까지 도달 못함
            count = 0
            break
        # 여기서 break되지 않았다면 다음 정류장까지 가는 것은 가능하다는 뜻

        if stops[i] > position + K: # 내가 충전한 곳에서 K만큼 더 했는데 못간다
            # 이전 정류장에서 충전을 해야한다는 뜻
            count += 1
            position = stops[i-1] # 현재 위치를 이전 정류장으로 하겠다는 뜻

    print(f'#{tc} {count}')