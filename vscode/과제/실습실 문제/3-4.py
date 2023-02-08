blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
types = list(set(blood_types))
types.sort()
typecount = []
for type in types:
    typecount.append(blood_types.count(type))

# print(types)
# print(typecount)

blood_dict = dict(zip(types, typecount))
print(blood_dict)