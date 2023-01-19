def my_magic_func(n):
    return n * 10


map_obj = map(my_magic_func, [1, 2, 3])
rlt = list(map_obj)

print(rlt)
# 위의 함수를 한번만 쓰고 버릴건데 정의를 하는데 너무 번거로워

# lambda 매개변수 : 매개변수를 이용한 리턴 값
lambda x: x * x

def pow(x):
    return x * x
# 위의 두 함수는 같은 기능을 함

# lambda 실행
print((lambda x: x * x)(4)) # print(f(x))와 같음

my_func = lambda n: n * 2 # 변수에 저장하고
my_func(2) # 이런식으로 활용할 수 있다.