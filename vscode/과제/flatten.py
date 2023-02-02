for t in range(1, 11):
    N = int(input())
    boxlist = list(map(int, input().split()))
    for n in range(N):
        for j in range(0, len(boxlist) - 1):
            min_idx = j
            for i in range(j, len(boxlist)):
                if boxlist[i] < boxlist[min_idx]:
                    min_idx = i
            boxlist[j], boxlist[min_idx] = boxlist[min_idx], boxlist[j]
            # 정렬하고
        # 제일 끝에 있는거 -1 제일 앞에 있는거 +1
        boxlist[0] = boxlist[0] + 1
        boxlist[-1] = boxlist[-1] - 1

    result = boxlist[-2] - boxlist[1]
    print(f'#{t} {result}')