scores = [('eng', 88), ('sci', 90), ('math', 80)]
# 정렬
print(scores)
scores.sort()
print(scores)
# [('eng', 88), ('sci', 90), ('math', 80)]
# [('eng', 88), ('math', 80), ('sci', 90)]
# 맨 앞의 값 기준으로 정렬됨

# 숫자 기준으로 정렬하려면 어떻게 해야 될까?
def check(x):
    return x[1]

print(scores)
scores.sort(key=check) # 콜백함수로 check를 사용하란 뜻
print(scores)

# check 함수는 sort 안에서 한번만 사용한다
# 이럴 때 람다 함수를 사용한다
print(scores)
scores.sort(key=lambda x: x[1])
print(scores)