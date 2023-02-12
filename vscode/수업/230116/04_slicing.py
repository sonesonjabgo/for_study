# 슬라이싱 연습
arr = [0,1,2,3,4,5,6,7,8,9,10]
# 시퀀스[start:end:step]
# start와 step은 생략 가능

a = arr[4:]
print(a)  # [4, 5, 6, 7, 8, 9, 10]
# 4번부터 잘라서 복사
# start를 포함한다.
# end 생략

b = arr[:4]
print(b)
# 4번 이전까지 잘라서 복사
# end는 포함 안함
# start 생략

c = arr[:]
print(c)
# 처음부터 끝까지 잘라서 복사
# start, end 둘 다 생략

lst = [1,2,3]
lst1 = lst
lst[0] = 100
print(lst)   # [100,2,3]
print(lst1)  # [100,2,3]
# 두개 다 바뀐 것처럼 보이지만 사실 리스트는 하나밖에 존재하지 않음

lst = [1,2,3]
lst1 = lst[:]
lst[0] = 100
print(lst)   # [100,2,3]
print(lst1)  # [1,2,3]
# 슬라이싱을 하면 복사해서 리스트가 하나 더 생성되는 것
# 그래서 lst 와 lst1은 다른 리스트이다.

d = arr[::-1]
print(d) # [10,9,8,7,6,5,4,3,2,1,0]