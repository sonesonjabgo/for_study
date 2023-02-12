# KMP 활용
T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    N = len(A)
    M = len(B)
    lps = [0] * (M+1)
    lps[0] = -1

    i = 0
    j = 0
    count = 0
    while i < N and j <= M:
        if j == -1 or A[i] == B[j]:
            i += 1
            j += 1
        else:
            j = lps[j]
        if j == M: # 일치 했을 때
            count += 1
            j = lps[j]

    new_A = A.replace(B, '')
    num = len(new_A)
    result = num + count
    print(f'#{tc} {result}')

