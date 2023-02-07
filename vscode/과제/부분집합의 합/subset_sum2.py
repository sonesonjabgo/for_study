import sys
sys.stdin = open("sample_input (2).txt", "r")

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    my_list = [x for x in range(1, 13)]  # 1부터 12까지 원소를 가지고 있는 리스트
    result = 0
    for i in range(1<<12):
        count = 0
        sum_num = 0
        for j in range(12):
            if i & (1<<j): # 2**12의 부분집합들 중에
                count += 1
                sum_num += my_list[j]
        if (count == N) and (sum_num == K):
            result += 1

    print(f'#{t} {result}')