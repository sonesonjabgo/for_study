# 재귀 함수
# 자기 자신을 호출하는 함수

def recur():
    print('뿅')
    recur()

recur() # 무한 반복하다가 에러

# 어디에 사용하는가?
# 재귀함수를 사용했을 때 명시적으로 로직을 표현할 수 있을 때

# 5! = 5 * 4 * 3 * 2 * 1
def fac(n):
    if n == 0: # 0이 되면 끝내야 함 / 이 부분 중요 (언제 끝날건지)
        return 1 # 0! 은 1 
    return n * fac(n - 1) # fac(n - 1)을 통해 n의 값을 낮춰고 자기 자신을 호출

# 재귀함수는 한계가 없기 때문에 머리 속에서 정리하기 힘들다
# 손으로 써보면서 정리하도록 하자

# 실행은 위에서부터 되지만
# 끝나는 건 뒤쪽에서 먼저 끝나서 계산은 뒤쪽부터 시작됨
# 이 구조를 이해하려면 손으로 적어보는 것이 필요
