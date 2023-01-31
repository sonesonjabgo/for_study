# 상속 관련 함수와 메서드
# isinstance(object, classinfo)
# classinfo의 instance거나 subclass*인 경우 True
class Person:
    pass

class Professor(Person):
    pass

class Student(Person):
    pass

# 인스턴스 생성
p1 = Professor()
s1 = Student()

print(isinstance(p1, Person)) # True
print(isinstance(p1, Professor)) # True
print(isinstance(p1, Student)) # False

# issubclass(class, classinfo)
# class가 classinfo의 subclass면 True
# classinfo의 모든 항목을 검사

print(issubclass(bool, int)) # True
print(issubclass(float, int)) # False
print(issubclass(Professor, Person)) # True

