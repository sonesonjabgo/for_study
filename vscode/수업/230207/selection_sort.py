# 선택 정렬
# 목적은 배열의 인덱스를 잘 활용하는 연습을 하자
# 알고리즘 설명
# 각 자리에 맞는 수를 선택해서 자리에 넣어주고
# ex) 제일 앞자리에는 제일 작은 수 선택해서 넣어주기
# 0번 부터 N=2번까지 자리에 들어갈 요소 선택해서 넣어주기
# 마지막은 어차피 가장 큰 수이기 때문에 검사할 필요 없음
arr = [5,6,1,4,3,7,8,2,9]
N = 9
for i in range(N-1):
    for i in range(N-1):
        # 1번 부터, N-1번 요소 중에 제일 작은애 찾기
        min_idx = i
        for j in range(i+1,N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

print(arr)