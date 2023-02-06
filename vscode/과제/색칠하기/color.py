# 테스트 케이스
# 영역의 개수
# 영역 정보
import sys
sys.stdin = open("sample_input(11).txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    count = 0  # 겹치는 범위가 하나 있을 때 마다 1 상승
    # 10 * 10 행렬
    arr = [[0 for _ in range(10)] for _ in range(10)]
    for n in range(N):
        info = list(map(int, input().split()))
        # 빨간색 범위와 파란색 범위가 겹치는 부분을 구해야 함
        for i in range(info[1], info[3]+1): # 열 길이 만큼 반복
            for j in range(info[0], info[2]+1): # 행 길이 만큼 반복
                arr[i][j] += info[4] # 해당하는 범위에 해당하는 색깔 칠하기

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                count += 1
        # 행렬을 전부 행 우선 순회로 돌아서 보라색(3)인 부분의 개수를 찾는다.
    print(f'#{t} {count}')