
mn = 100*100
si = 0
for sj in range(1, 101):
    cnt, dj = 0, 0
    # [1] 시작지점 찾기
    if arr[si][sj] != 1:
        continue
    ci, cj = si, sj
    while ci<99:
        cnt += 1
        if dj==0:
            if arr[ci][cj-1]==1: #좌측
                dj = -1
                cj -= 1
            elif arr[ci][cj+1]==1: #우측
                dj = 1
                cj += 1
            else:
                ci += 1

        else:
            if arr[ci][cj+dj]==1:
                cj+=dj
            else:
                dj=0
                ci+=1
    if mn>=cnt:
        mn, ans = cnt, sj-1