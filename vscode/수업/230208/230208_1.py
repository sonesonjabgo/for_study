# itoa, atoi 함수 만들어보기
print(ord('1'))
# '123' >>> 123
# 문자 받아와서 숫자로 반환하기
def atoi(data):
    result = 0
    
    # '1' > 1 >> 저장
    # '2' > 2 >> 기존값 * 10  + 2 >> 저장
    # '3' > 3 >> 기존값 * 10  + 3 >> 저장
    for i in range(len(data)):
        result = result * 10 + ord(data[i]) - ord('0')
        # ord(data[i]) - ord('0') i가 1이라면 49 - 48 이고 값이 1이 나옴
    return result

result = atoi('45421')
print(result, type(result))

# 숫자를 문자열로 만들기
def itoa(data):
    result = ''
    # 숫자의 각 자리를 떼어내기, 10으로 나눈 나머지 바꾸기
    # data를 10으로 나눈 몫과 나머지로 떼냄
    # data가 0이 되기 전이라면 계속 반복
    while data > 0:
        remain = data % 10
        result = chr(remain + ord('0')) + result
        data = data // 10
    return result
    # 3 + 48 = 51
    # chr(51) = '3'
    # 기존의 문자열 앞 쪽에 새로 변환한 숫자가 들어와야 함

rst = itoa(33551)
print(rst, type(rst))