# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 반드시 재귀함수로 구현해야 합니다.
def dec_to_bin(number):
    # number가 1이 될 때까지 2로 계속 나눈다
    # 몫은 계속 나누도록 하고 나머지는 저장
    # % 한 값이 True일 때 문자열 1을 리스트에 저장하고
    # False일 때 0을 저장
    rltlist = []
    if number % 2: # 홀수고 1을 저장해야 함
        divnum = number // 2
        rltlist.append(1)
    else:
        divnum = number // 2
        rltlist.append(0)
    dec_to_bin(divnum)
    # 이따 수정


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010
