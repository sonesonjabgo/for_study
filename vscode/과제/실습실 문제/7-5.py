# 고쳐야됨


import random
class ClassHelper:
    def __init__(self, namelist):
        self.namelist = namelist
    
    def pick(self, n):
        return random.choice(self.namelist, n)

    def match_pair(self):
        random.shuffle(self.namelist)
        stu_list = []
        while len(self.namelist) == 0:
            student1 = self.namelist.pop()
            student2 = self.namelist.pop()
            stu_list.append([student1, student2])

            if len(self.namelist) == 3:
                stu_list.append(self.namelist[:])
            
        return stu_list



ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

print(ch.match_pair())
print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())
