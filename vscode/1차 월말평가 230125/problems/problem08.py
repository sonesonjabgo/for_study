# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    # map 함수로 각각의 문자를 ord를 사용해서 알파벳을 숫자로 만들어준다.
    # 그리고 나서 숫자에 n을 더한 후 다시 알파벳으로 만들고
    # 모든 알파벳을 붙여서 return
    # 대문자의 경우 90 소문자의 경우 122 가 넘을 때 각각 65, 97부터 다시 시작해야 함
    # 대소문자 확인 필요, 오버할 시에 다시 처음부터 시작하는 방법 있어야 함.
    # 이건 숫자로 바꾸고 if문으로 넣기
    # P에 17을 더하면 97이 돼서 a가 됨
    # 의도한 바는 90이 넘어가면 90 뺀 7만큼 65에서 시작해서
    # H가 나와야 함
    # 그러면 우선적으로 개별 word가 대소문자 구분을 하고
    # 대문자일 경우 90이 넘었을 때 chgnum에 90을 뺀 값을 65에 더해준다
    # 소문자일 경우 122가 넘었을 때 
    # 한 글자씩 떼와서 대소문자 구분하고 숫자 바꿔서 더하고 오버하는 지 확인하고 처리하고 리스트에 저장
    str_list = []
    for str in word: # word의 한 글자씩 떼오겠다
        chgnum = ord(str) + n # 알파벳을 숫자로 바꿔서 입력한 n을 더하겠다
        if str.islower(): # str이 소문자라면
            # 여기에 122 넘었을 때 97+(chgnum-122)가 들어가야 함
            if chgnum > 122:
                chrstr = chr(96+(chgnum-122))
            else:
                chrstr = chr(chgnum)
        else: # 대문자라면
            if chgnum > 90:
                chrstr = chr(64+(chgnum-90))
            else:
                chrstr = chr(chgnum)
        str_list.append(chrstr)
    my_str = ('').join(str_list)
    return my_str

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
