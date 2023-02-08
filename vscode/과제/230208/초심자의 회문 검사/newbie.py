import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    word = input()
    count = 0
    for i in range(len(word)):
        if word[i] == word[-(i+1)]:
            count += 1
    if count == len(word):
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')