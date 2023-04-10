def cal_(a,b):
    asum=0
    for i in a:
        for j in a:
            if i==j:
                continue
            asum+=data[i][j]
    bsum=0
    for i in b:
        for j in b:
            if i==j:
                continue
            bsum+=data[i][j]
    ansArr.append(abs(asum-bsum))


def team(n, start, link):
    # 조합을 사용해 player 중 3개(N//2개)를 start에 넣는다.
    # 나머지 숫자들은 link로
    if n == N//2:
        # start에 들어가 있는 숫자가 아니면 link에 넣기
        for i in range(1, N+1):
            if i not in start:
                link.append(i)

        print(start, link)
        cal_(start, link)

    for j in range(1, N+1):
        if not selected[j]:
            selected[j] = 1
            start.append(j)
            team(n+1, start, link)
            start.pop()
            selected[j] = 0

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

selected = [0] * (N+1)
ansArr=[]
team(0, [], [])
print(min(ansArr))