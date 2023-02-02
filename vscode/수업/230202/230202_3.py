# 완전 검색
# 1. 모든 순서 다 바꾸기
# 앞 절반 뒤 절반 run, triplet 검사
# 순서는 어떻게 바꾸지?
# 세 개 짜리로 한 번 바꿔 봅시다
# 0 ~ 2 까지의 수
# for i in range(3): # 0,1,2 i: 첫 번째 자리
#     for j in range(3): # j: 두 번째 자리
#         for k in range(3): # k: 세 번째 자리
#              print(i, j, k)  # 모든 경우의 수 출력
# 근데 숫자 서로서로 같으면 안됨

# for i in range(3): # 0,1,2 i: 첫 번째 자리
#     for j in range(3): # j: 두 번째 자리
#         if i == j: # i와 j가 같으면 다음 반복문 실행
#             continue
#         for k in range(3): # k: 세 번째 자리
#             if i == k or j == k:
#                 continue
#             print(i, j, k)  # 모든 경우의 수 출력
# 순열이 생성됨

# 여기에다가 바꾸고 싶은 리스트가 있다면
# 끝의 프린트 문만 바꿔주면 됨
arr = [5, 7, 6]
for i in range(3): # 0,1,2 i: 첫 번째 자리
    for j in range(3): # j: 두 번째 자리
        if i == j: # i와 j가 같으면 다음 반복문 실행
            continue
        for k in range(3): # k: 세 번째 자리
            if i == k or j == k:
                continue
            print(arr[i], arr[j], arr[k])  # 모든 경우의 수 출력

# baby-gin의 run이나 triplet을 찾고 싶을 때
arr = [5, 7, 6]
for i in range(3): # 0,1,2 i: 첫 번째 자리
    for j in range(3): # j: 두 번째 자리
        if i == j: # i와 j가 같으면 다음 반복문 실행
            continue
        for k in range(3): # k: 세 번째 자리
            if i == k or j == k:
                continue
            print(arr[i], arr[j], arr[k])  # 모든 경우의 수 출력
            if arr[i] == arr[j]-1 and arr[i] == arr[k]-2
                print('run!')
            elif arr[i] == arr[j] and arr[i] == arr[k]:
                print('triplet!')

# 이제 baby-gin에 맞는 6개의 숫자로
arr = [3,2,1,3,4,5]
for i in range(6): # 0,1,2 i: 첫 번째 자리
    for j in range(6): # j: 두 번째 자리
        if i == j: # i와 j가 같으면 다음 반복문 실행
            continue
        for k in range(6): # k: 세 번째 자리
            if i == k or j == k:
                continue
                # 여기에 추가로 3개의 숫자가 있어야 함.
            for a in range(6):
                if a == i or a == j or a == k:
                    continue
                for b in range(6):
                    if b == a or b == i or b == j or b == k:
                        continue
                    for c in range(6):
                        if c == b or c == a or c == i or c == j or c == k:
                            continue
                            # 여기까지가 주어진 수로 수열 생성