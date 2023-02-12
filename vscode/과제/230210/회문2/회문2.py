import sys
sys.stdin = open("input.txt", "r")

for _ in range(1, 11):
    test_case = int(input())
    a = [input() for _ in range(100)]
    result = []
    for M in range(100, 1, -1):
        for i in range(100):
            for j in range(100-M+1):
                for k in range(M//2): # 절반만 검사해도 되기에
                    if a[i][j+k] != a[i][j+M-1-k]:
                        break
                else:   # 검사를 했는데 전부 맞아서 회문일 때
                    result.append(M)      # 회문의 길이를 가져감
        #####################################################
                for k in range(M//2):
                    if a[j+k][i] != a[j+M-1-k][i]:
                        break
                else:
                    result.append(M)

    print(f'#{test_case} {result[0]}')