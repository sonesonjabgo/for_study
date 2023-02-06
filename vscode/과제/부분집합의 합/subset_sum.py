import sys
sys.stdin = open("sample_input (2).txt", "r")

T = int(input())
my_list = [x for x in range(1, 13)] # 1부터 12까지 원소를 가지고 있는 리스트
for t in range(1, T+1):
    count = 0
    N, K = map(int, input().split())
    for i in range(1 << 12): # 모든 부분집합을 만듦
        for j in range(12): #
            if i & (1 << j):
                count += 1
    print(f'#{t} {count}')

# 모든 부분 집합을 검사해서 요소가 N개 들어가는 것 찾고
# 그 요소의 합이 K인 것을 찾아야 한다.
