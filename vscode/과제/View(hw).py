# 건물의 개수 N개
# 테스트 케이스 10회

for testcase in range(1,11):
    N = int(input())
    building = list(map(int, input().split())) # 빌딩 각각의 높이
    totalview = 0
    for n in range(3, N-2): # 앞의 두 곳과 뒤의 두 곳을 제외하기 위해
        if building[n-1] >= building[n-2]:
            leftview = building[n] - building[n-1]
        else:
            leftview = building[n] - building[n-2]

        if building[n + 1] >= building[n + 2]:
            rightview = building[n] - building[n + 1]
        else:
            rightview = building[n] - building[n + 2]
        print(leftview, rightview)
        if rightview <= 1 or leftview <= 1:
            view = 0
        else:
            if rightview > leftview:
                view = leftview
            else:
                view = rightview
        totalview += view
    print(f'#{testcase} {totalview}')