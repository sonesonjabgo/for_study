i = 0
while i<N:
    # 1. i ~ 끝까지 최대값의 index 찾기
    i_mx = i
    for j in range(i+1, N):
        if lst[i_mx] < lst[j]:
            i_mx = j
    # 2. i~i_mx 까지의 최대값의 차이 누적