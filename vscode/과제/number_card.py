# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오
# 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

# 테스트 케이스 개수 T  (1 <= T <= 50)
# 주어질 카드의 수 N (5 <= N <= 100)
# N개의 숫자 여백없이 주어짐 card

# 카운팅 정렬의 빈도 수를 알아낸 뒤 그 중 값이 가장 높은 것
# 그 중 숫자가 제일 높은 것

T = int(input())

for t in range(1, T+1):
    N = int(input())
    cards = input()
    num = [0] * 10  # cards의 요소를 인덱스로 넣어 숫자를 하나씩 올릴 것임.
    for card in cards: # 4 9 6 7 9
        num[int(card)] += 1
    maxnum = 0
    index = 0
    for i in range(len(num)): # 0 1 2 3 4 5 6 7 8 9
        if num[i] >= maxnum:
            maxnum = num[i]
            index = i
    print(f'#{t} {index} {maxnum}')