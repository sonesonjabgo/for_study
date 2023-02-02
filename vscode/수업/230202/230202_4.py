# 탐욕 방법
# 현재 상태에서 내가 할 수 있는 가장 좋은 것을 선택하는 방법
# 숫자 개수 세기
# 앞에서 부터 run인지 triplet인지 검사하면서 뒤로 이동
# 단, triplet부터 검사해야 한다.
# 숫자 세기
arr = [3,2,1,3,4,5]
count = [0] * 10
for i in range(len(arr)):
    count[arr[i]] += 1  # 개수 세기

# 앞에서 부터 보면서 run, triplet 검사하기
run_cnt = 0 # run일 때 +1
tri_cnt = 0 # triplet일 때 +1
i = 0
while i < len(count):
# for i in range(len(count)):
    if count[i] >= 3: # triplet 검사
        tri_cnt += 1
        count[i] -= 3 # triplet일 때 해당 i의 개수 3개 빼줘야 함
        i -= 1 # 원래자리 한 번 더 검사하려고 뺌
    elif count[i] > 0: # run 검사
        if i <= 7 and count[i+1] and count[i+2]: # 계수가 있다는 건 해당 리스트에 1개 이상 존재한다는 것
            run_cnt += 1
            count[i] -= 1
            count[i+1] -= 1
            count[i+2] -= 1  # run으로 활용했으니 1씩 빼줘야 함
            i -= 1  # 원래자리 한 번 더 검사하려고 뺌
    i += 1

if run_cnt + tri_cnt == 2:
    print('baby gin이다')
else:
    print('baby gin 아니네')