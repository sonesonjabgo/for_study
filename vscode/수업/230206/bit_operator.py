arr = ['a', 'b', 'c']
# 모든 부분집합을 구하기 위해서 비트를 활용하자

N = 3
# for i in range(2**N):
for i in range(1<<N):
    # i : 0~2**N-1, i의 비트 모양이 부분집합의 모양이다.
    # i의 모든 비트를 확인하자
    print(i)
    for j in range(N):
        # i&(1 << 0)
        # i&(1 << 1)
        # i&(1 << 2)
        # i&(1 << 3)
        # 이것을 요소의 개수 N개 만큼 반복
        if i & (1 << j) != 0: # 0이 아니다라는 것을 찾으면 j번째 비트가 해당 부분집합이라는 뜻
            print(arr[j], end=' ')
    print()