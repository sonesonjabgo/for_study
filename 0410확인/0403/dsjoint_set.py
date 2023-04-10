# 서로소 집합 : 서로소 집합들은 서로 중복된 원소를 포함하지 않음
# make_set, find_set, union 등의 연산이 가능합니다.
# 원소의 개수는 10개라고 가정

def make_set():
    return [x for x in range(7)]

p = make_set()  # 인덱스에 해당하는 요소의 부모요소 번호를 가지는 배열

# 집합의 대표자를 반환하는 함수
# 대표자 : 부모의 번호와 자신의 번호가 일치하는 요소
def find_set(x):
    if x == p[x]: # 내가 대표자면 반환
        return x
    else: # 아니면.. 부모가 대표자를 알고 있을 것)
        return find_set(p[x])
    
# 두 개의 집합을 합침
def union(x, y): 
    rx = find_set(x) # x의 대표자
    ry = find_set(y) # y의 대표자
    if rx != ry:
        # 합치는 방식은 많을 수 있는데..
        # 일단은 쉽게 y의 대표자의 부모를 x의 대표자로 만들기
        p[ry] = rx

print(p)
union(1,3)
print(p)
union(2,3)
print(find_set(6))
print(p)