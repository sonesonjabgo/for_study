import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = list(input())
    M = list(input())
    max = 0
    for i in N:
        count = 0
        for j in M:
            if i == j:
                count += 1
                if count > max:
                    max = count
    print(f'#{test_case} {max}')