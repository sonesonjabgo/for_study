# 비정상적 암호 존재 가능

# 일단 배열에서 16진수로 된 암호 찾기
# 16진수에서 2진수로 변경
# 2진수를 8자리로 나눠서 암호 딕셔너리에 있는 지 확인
# 하나라도 없을 경우 불량
# 다 있으면 홀 짝 나눠 더해서 불량 확인

dic = {'0' : '0000', '1' : '0001', '2' : '0010', '3': '0011', '4' : '0100',
       '5' : '0101', '6' : '0110', '7' : '0111', '8' : '1000', '9' : '1001',
       'A' : '1010', 'B' : '1011', 'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111'
       }

code_num = {
    (3, 2, 1, 1): '0',
    (2, 2, 2, 1): '1',
    (2, 1, 2, 2): '2',
    (1, 4, 1, 1): '3',
    (1, 1, 3, 2): '4',
    (1, 2, 3, 1): '5',
    (1, 1, 1, 4): '6',
    (1, 3, 1, 2): '7',
    (1, 2, 1, 3): '8',
    (3, 1, 1, 2): '9'
}

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]

    trans = [] # 2진수로 변환한 숫자
    for i in range(N):
        ro = ''
        for j in range(M):
            ro += dic[data[i][j]]
        trans.append(ro)


    password_lst = []
    for i in range(N):
        for j in range(M*4-1, 54, -1):
            if trans[i][j] == '1':  # 암호코드의 시작점을 찾음!
                idx = j
                password = ''

                for _ in range(8):
                    # 56개비트를 7개끊어 읽어서 8개 숫자 찾기
                    w1 = w2 = w3 = w4 = 0  # 0과 1의 너비를 저장하기 위한 변수
                    # 1의 개수 세기 > w4
                    while trans[i][idx] == '1':
                        w4 += 1
                        idx -= 1
                    # 0의 개수 세기 > w3
                    while trans[i][idx] == '0':
                        w3 += 1
                        idx -= 1
                    # 1의 개수 세기 > w2
                    while trans[i][idx] == '1':
                        w2 += 1
                        idx -= 1
                    w1 = 7-(w2+w3+w4)
                    idx -= w1     #다음 숫자 마지막 1로 위치 옮기기

                    mn = min(w1, w2, w3, w4)
                    # print((w1, w2, w3, w4))
                    # print(code_num[w1, w2, w3, w4])
                    # print(mn)
                    last = (w1 // mn, w2 // mn, w3 // mn, w4 // mn)
                    password += code_num[last]
                password_lst.append(password)


    print(password_lst)
    # hol = 0
    # jjak = 0
    # for i in range(7, 0, -1):
    #     if i % 2:
    #         hol += password[i]
    #     else:
    #         jjak += password[i]
    #
    # if (hol * 3 + jjak) % 10 + password[7] == 0:
    #     print(f'#{tc} {hol + jjak + password[7]}')