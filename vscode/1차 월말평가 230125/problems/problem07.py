# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calculator(*numbers):
    # numbers의 개수를 파악하는 것이 첫번째
    # numbers의 개수가 1개일 때는 원의 넓이를 반환
    # numbers의 개수가 2개일 때 밑변과 높이
    # numbers의 개수가 3개 이상 모든 입력의 합과 평균을 튜플로 반환
    my_cal = 0
    pi = 3.14
    if len(numbers) == 1:
        my_cal = numbers[0]**2 * pi
    elif len(numbers) == 2:
        sum_num = sum(numbers)
        if sum_num % 2:
            my_cal = (numbers[0] * numbers[1])/2
        else:
            my_cal = numbers[0] * numbers[1]
    elif len(numbers) >= 3:
        my_cal = (sum(numbers), sum(numbers)/len(numbers))
    return my_cal



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0