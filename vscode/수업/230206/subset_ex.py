# # 부분집합 합
# a = [1,2,3,4]
# # 집합 a의 모든 부분집합 출력하기
# # 알고리즘 해를 구할 때 일반적으로 쓰이는 완전 탐색

# a의 부분집합 개수는 2**(len(a))
bit = [0,0,0,0]
# 부분집합 생성
for i in range(2): # i = 0 or 1
    bit[0] = i 
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)
# 집합에 요소 포함 여부 결정
