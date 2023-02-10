import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    numbers = [list(map(int, input().split())) for _ in range(9)]
    # print(numbers)
    result = True
    # 행 검사
    for number in numbers:
        if len(set(number)) != 9:
            result = False

    # 열 검사
    numbers_t = list(zip(*numbers))
    for number in numbers_t:
        if len(set(number)) != 9:
            result = False

    # 칸 검사
    check = []
    for i in range(0,3,6):
        for j in range(0, 3, 6):
            for k in range(3):
                for l in range(3):
                    check.append(numbers[i+k][j+l])
        if len(set(check)) != 9:
            result = False

    if result:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
