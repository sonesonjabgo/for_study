import sys
sys.stdin = open("Factorization.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [2, 3, 5, 7, 11]
    empty = [0, 0, 0, 0, 0]
    for i in range(len(arr)):
        while N % arr[i] == 0: # N이 arr[i]로 나뉠 때 진행
            N = N // arr[i] # N에 arr[i]로 나눈 몫을 저장
            empty[i] += 1   # arr[i]의 제곱수를 저장하는 것임
            # 몫이 저장된 N이 다시 while을 진행해 arr[i]로 나누게 된다
            result = ' '.join(map(str, empty))

    print(f'#{t} {result}')