list1 = [1,2,3,1,1]
a = tuple(list1)
b = set(list1)
print(a,b)

range1 = range(5)
a = list(range1)
b = tuple(range1)
c = set(range1)
print(a,b,c)

set1 = {1,2,3,4,5,6}
a = list(set1)
b = tuple(set1)
print(a,b)

dict1 = {
    'key1' : 'value1',
    'key2' : 'value2',
    'key3' : 'value3',
    'key4' : 'value4'
}

a = list(dict1)
b = tuple(dict1)
c = set(dict1)

print(a,b,c)