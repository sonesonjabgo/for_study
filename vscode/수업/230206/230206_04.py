# bit = [0, 0, 0, 0]
# for i in range(2):
#     bit[0] = i                  # 0번째 원소
#     for j in range(2):
#         bit[1] = j              # 1번째 원소
#         for k in range(2):
#             bit[2] = k          # 2번째 원소
#             for l in range(2):
#                 bit[3] = 1      # 3번째 원소
#                 print(bit)          # 생성된 부분집합 출력

A = [1, 2, 3, 4]
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i                  # 0번째 원소
    for j in range(2):
        bit[1] = j              # 1번째 원소
        for k in range(2):
            bit[2] = k          # 2번째 원소
            for l in range(2):
                bit[3] = 1      # 3번째 원소
                print(bit, end=' ')
                s = 0
                for p in range(4):
                    if bit[p]:
                        print(A[p], end= ' ')
                        s += A[p]
                print(s)