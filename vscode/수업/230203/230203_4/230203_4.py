# 1208. Flatten
# 가장 높은 곳에서 1빼고 가장 낮은 곳에서 1더하면 되는 문제
# 어디가 제일 높은지 어디가 제일 낮은지만 알면 됨
import sys
sys.stdin = open('1208_input.txt')
for tc in range(1, 11): # 이따 출력을 1부터 해야해서 1부터 시작
    N = int(input())
    boxes = list(map(int(input().split())))
    # 1. 덤프
    #   1-1 최고 높이 위치찾기
    #   1-2 최저 높이 위치찾기
    for _ in range(N):
        max_idx = 0
        min_idx = 0
        for i in range(100): # 가로길이 100으로 고정되어 있음
            if boxes[max_idx] < boxes[i]:
                max_idx = i
            elif boxes[min_idx] > boxes[i]:
                min_idx = i
        #   1-3 최고 높이에서 -1, 최저높이에서 +1
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
    # 2. 1을 N번 반복
    # 3. 결과출력 (최고높이-최저높이)
    max_idx = 0
    min_idx = 0
    for i in range(100):  # 가로길이 100으로 고정되어 있음
        if boxes[max_idx] < boxes[i]:
            max_idx = i
        elif boxes[min_idx] > boxes[i]:
            min_idx = i
    print(f'#{tc} {boxes[max_idx] - boxes[min_idx]}')