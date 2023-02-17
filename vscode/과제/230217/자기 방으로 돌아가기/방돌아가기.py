import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    stu = [list(map(int, input().split())) for _ in range(N)]

    count = [0] * 201 # 0번은 제외하고 1번방 부터 200번 방까지
    # 방을 옮기는데 복도를 사용하면서 지나가는 곳은 1씩 더한다.

    for j in range(N):
        # start = end = 0
        if stu[j][0] % 2:
            start = stu[j][0] // 2 + 1
        else:
            start = stu[j][0] // 2

        if stu[j][0] % 2:
            end = stu[j][1] // 2 + 1
        else:
            end = stu[j][1] // 2

        if start > end:
            start, end = end, start

        for i in range(start, end+1):
            count[i] += 1
    # print(count)
    max_c = count[0]
    for i in range(len(count)):
        if count[i] > max_c:
            max_c = count[i]

    print(f'#{test_case} {max_c}')