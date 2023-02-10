T = int(input())
for t in range(1, T+1):
    # 전체 쪽수 end, 찾으려는 번호 A, B
    end, A, B = map(int, input().split())
    start = 1

    # 이진 탐색 함수 만들기
    def binary_search(s, F, e):
        count = 0
        while True:
            count += 1
            mid = int((s + e) / 2)
            if F > mid:
                s = mid + 1 - 1 # 책이니까 한 면당 페이지가 두개 존재하잔아
            elif F < mid:
                e = mid - 1 + 1 # 책이니까 한 면당 페이지가 두개 존재하잔아
            else: # F == mid
                return count

    Arst = binary_search(start, A, end)
    Brst = binary_search(start, B, end)

    if Arst < Brst:
        print(f'#{t} A')
    elif Arst > Brst:
        print(f'#{t} B')
    else:
        print(f'#{t} 0')