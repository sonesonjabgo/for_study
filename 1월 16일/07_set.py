# set
# 집합 자료형
# 중복되지 않는 데이터를 가지는 자료형
# 시퀀스 아님 가변형
# {} < 얘는 딕셔너리라서 set() 함수 이용해야 함
a = set()
print(type(a))
a.add(1)
a.add(2)
a.add(3)
a.add(1)
print(a)
# 1을 두개 집어넣음에도 하나 나옴
# 중복되지 않는 값을 가진다.
