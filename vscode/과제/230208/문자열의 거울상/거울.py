import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    str_dict = {'b':'d', 'd':'b', 'p':'q', 'q':'p'}
    str1 = input()
    str2 = ''
    for i in range(len(str1)):
        mirror = str_dict[str1[i]] # d로 바꾸어서
        str2 = mirror + str2
    print(f'#{test_case} {str2}')