def team(n, start, link):
    # 조합을 사용해 player 중 3개(N//2개)를 start에 넣는다.
    # 나머지 숫자들은 link로
    if n == N//2:
        # start에 들어가 있는 숫자가 아니면 link에 넣기
        for i in range(1, N+1):
            if i not in start:
                link.append(i)
            # 이후로 최소 신장 트리를 만들어서 return으로 값을 내준다..
        return start, link

    for j in range(1, N+1):
        if not selected[j]:
            selected[j] = 1
            start.append(j)
            team(n+1, start, link)



# 최소 신장 트리 문제
# 스타트 팀과 링크 팀에 속해있는 노드들 잇는 간선의 정보 (가중치)가 주어짐
# >> 유방향 그래프
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

# 일단 N//2 씩 팀을 두팀으로 나눠야 함
# 모든 경우의 수를 고려
# 그리고 prim 알고리즘을 통해 최소 신장 트리를 구하고
# 해당 값이 최소값이라면 저장 아님말고

# player = [n for n in range(1, N+1)]
selected = [0] * (N+1)