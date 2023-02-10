# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    arr = [input() for _ in range(5)]
    for i in range(5):
        if len(arr[i]) < 15:
            less = 15 - len(arr[i])
            arr[i] = arr[i] + '_' * less
    result1 = ''
    for j in range(15):
        for k in range(5):
            result1 += arr[k][j]
    
    modi = list(result1)
    result = ''
    for l in range(len(modi)):
        if modi[l] != '_':
            result += modi[l]
    
    print(f'#{test_case} {result}')