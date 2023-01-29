# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 반드시 재귀함수로 구현해야 합니다.
def dec_to_bin(number):
    rltlist = []
    while number:  # number가 0이 아니면 반복문 실행
        if number != 1:  # number가 1이 아니면 2로 나눴을 때 몫이 존재
            rltlist.append(str(number % 2)) 
            # 2로 나눴을 때 짝수면 0 홀수면 1을 저장
            number = number // 2 # number에 number를 2로 나눈 몫을 저장
            dec_to_bin(number) # 재귀함수로 
            # number에 들어가는 숫자가 2로 몇번 나눠질지 모르기 때문에 재귀함수 사용해야 한다.
        else: # number가 1일 경우 더 이상 2로 나눠질 수 없다
            rltlist.append(str(1)) # 남은 숫자인 1을 더해야 한다
            break # 반복문 종료
    rltlist.reverse() # 리스트에 저장한 나머지 1과 0을 거꾸로 나열해야 이진수
    return ''.join(rltlist)

# 의문 : 함수 안에 리스트를 선언해서 재귀함수를 통해 함수가 다시 실행되면
# rltlist가 빈 리스트가 되어야 하는 것이 아닌가?


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010
