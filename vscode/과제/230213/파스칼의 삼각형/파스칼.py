#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    for i in range(N):
        num = 2**i
        result = '1'
        while num != 1:
            num = num - i
            result = result + str(i)
        result = result + '1'
        print(result)