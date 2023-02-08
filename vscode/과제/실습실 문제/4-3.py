# 입력 예시
# [1, 1, 3, 3, 0, 1, 1]

# 출력 예시
# [1, 3, 0, 1]

# n = n+1 같을 때
# 333 일 경우 3,3

my_list = [1, 1, 3, 3, 0, 1, 1]


def solution(list):
    answer = [list[0]] # 입력된 리스트의 첫번째 요소
    for i in range(1, len(list)): # 입력된 리스트의 두번째부터 비교를 해야 하기 때문에
        if answer[len(answer)-1] == list[i]:
            continue
        answer.append(list[i])
    return answer

print(solution(my_list))