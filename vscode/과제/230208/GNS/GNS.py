T = int(input())
for _ in range(T):
    case = list(input().split())
    tc = case[0] # #1
    N = int(case[1]) # numbers의 총 개수
    num_dict = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
    numbers = list(input().split())
    # for i in range(len(numbers)):
    #     numbers[i] = num_dict[numbers[i]]
    for j in range(N-1):
        for i in range(0, N-1-j):
            if num_dict[numbers[i]] > num_dict[numbers[i+1]]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]


    print(tc)
    print(*numbers)