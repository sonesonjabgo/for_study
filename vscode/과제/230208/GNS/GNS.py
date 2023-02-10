T = int(input())
for _ in range(T):
    case = list(input().split())
    tc = case[0] # #1
    N = int(case[1]) # numbers의 총 개수
    num_dict = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}
    numbers = list(input().split())
    # for i in range(len(numbers)):
    #     numbers[i] = num_dict[numbers[i]]
    for j in range(N-1):
        for i in range(0, N-1-j):
            if num_dict[numbers[i]] > num_dict[numbers[i+1]]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]


    print(tc)
    print(*numbers)

#######
# 수업 시간에 한 것

T = int(input())
for _ in range(T):
    tc, N = input().split()
    N = int(N)
    nums = input().split()
    # 문자열 SVN, FOR 등등 크기 비교가 안되니
    # dictionary 이용해서 크기 비교하기
    num_dict = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5, 
    'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}

    # 정렬하기(버블, 선택정렬)
    # 선택정렬
    for i in range(N-1): # 0번 부터 N-1번 까지 들어가는 요소 찾기
        # i번째 들어갈 요소 찾아주기
        # : i번부터 맨뒷 요소중 제일 작은애
        min_idx = i # 제일 앞녀석이 제일 작다고 가정
        for j in range(i+1,N):
            # 그냥 비교가 안되니까 dictionary value로 비교하자
            if num_dict[nums[min_idx]] > num_dict[nums[j]]:
                min_idx = j
        # 원래 리스트를 정렬한다.
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    
    print(f'{tc}',*nums)