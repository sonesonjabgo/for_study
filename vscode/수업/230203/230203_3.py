# 9386 연속한 1의 개수

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))
    ans = cnt = 0
    # 변수 두개를 선언하는 이유는 ans에는 연속된 숫자의 최대값을 저장하기 위함이고
    # cnt는 연속된 숫자를 확인하기 위함이다.
    for i in range(N):
        if lst[i] == 0:
            cnt=0
        else: # lst[i]가 1일 때
            cnt+=1
            if ans<cnt: # 만약 ans가 cnt보다 작으면 연속된 숫자가 ans에 저장된 것 보다 큰 수가 나왔다는 것
                ans=cnt # ans에 더 높은 값을 저장