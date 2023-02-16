# 한 줄에 하나씩 숫자 뽑아서 최소값 만들기
# 세로 한줄에서 두 개 이상 뽑으면 안됨

#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    def dfs(start, N):
        # N=3이고 (0,0)에서 시작했다고 하면,
        # 0번 칼럼과 0번 인덱스에서 선택되면 안됨
        # 다음 선택지는 (1,1), (1,2)
        # 빈 행렬 만들어서 스택에 저장되면 빈 행렬에 해당 인덱스 값 1로 바꿈
        # 다음 선택은 0인 경우에서만 가능하게 함 > 이 조건을 위로 넣음 선택은 행렬에서 인덱스 값이 0인 경우만 가능
        # 해당 조건에서 만들 수 있는 모든 부분집합을 만들어야 함.
        # 스택에 선택한 인덱스 정보 저장
        # 선택이 끝나면 다시 stack의 top을 pop하고
        selected = [[0] * N for _ in range(N)] # 스택에 저장되면
        stack = [] # 선택한 인덱스 정보를 저장하기 위함
        stack.append(start)

        while stack:
            sr, sc = stack[-1]
            for i in range():
                for j in range():
                    selected[sr][i] = 1
                    selected[i][sc] = 1
            # stack의 top이 내가 가장 최근에 선택했던 행렬
            # sr, sc의 행렬과 그 전에 선택했던 행렬 선택 안되도록 해야 함
            for i in range():
                for j in range():
                    if i != sr and selected[i][j] != 1:
                        stack.append((i,j))
                        break
                        # 이렇게 하면 다음 줄의 모든 조건이 저장됨.
                        # 하나의 값만 저장하고 다음 행으로 넘어가야 함
                        # 값을 추가하고 반복문을 끝내면

#####################################################################################
N = 3 # 가정
arr = [
    [1,2,3],[4,5,6],[7,8,9]
]
min_sum = 1000
# idx 행의 몇 번째 열을 선택할건지 결정
selected = [0] * N # 행의 길이만큼 존재하면 됨. 몇 번째 행을 골랐는 지
used = [0] * N # 열의 사용 여부
min_sum = 10000
def solve(idx, sum_v):
    global min_sum
    if sum_v >= min_sum:
        # 중간합이 최솟값으로 두었던 것 보다 크면 진행할 필요 없다
        return
    if idx == N:
        # # 모든 행을 다 결정한 것
        # sum_v = 0
        # for i in range(N):
        #     selected[i] # i 행에서 선택한 열
        #         sum_v += arr[i][selected[i]]
        if min_sum > sum_v:
            min_sum = sum_v
        return
    # 내가 할 수 있는 모든 경우의 수 수행해보기
    for i in range(N): # i는 열의 번호, 모든 열 선택
        if not used[i]:
            selected[idx] = i
            used[i] = 1
            solve(idx+1, sum_v+arr[idx][i])
            # solve 함수는 idx 행의 몇 번째 열을 선택할건지 결정하는 함수
            used[i] = 0