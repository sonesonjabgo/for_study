import sys
sys.stdin = open("sample_input (2).txt", "r")

T = int(input())
my_list = [x for x in range(1, 13)] # 1부터 12까지 원소를 가지고 있는 리스트
for t in range(1, T+1):
    count = 0
    N, K = map(int, input().split())
    for i in range(1 << 12): # 모든 부분집합을 만듦
        for j in range(1 << N):
            if i & j:

    print(f'#{t} {count}')


