arr = [1,2,3,4,5]
N = len(arr)
selected = [0] % N

# idx 에 해당하는 요소가 부분집에 포함되는지 아닌지 결정
# 결정하고나서 다음 요소 포함여부 결정
def subset(idx):
    if idx == N:
        # N-1번 요소까지 결정이 끝난 상황
        print(selected)
        return
    # 완전탐색 : 내가 할 수 있는 것 모두해보기
    selected[idx] = 1
    subset(idx + 1)
    selected[idx] = 0
    subset(idx + 1)

subset(0)