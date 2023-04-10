def find_set(x):    # x가 속한 집합
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):    # y의 대표원소가 x의 대표원소
    rep[find_set(y)] = find_set(x)
    rep[y] = find_set(x)


# makeset
rep = [i for i in range(6)]
print(rep)