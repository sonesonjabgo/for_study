class Person:
    blood_color = 'red' # 클래스 변수 생성

    def __init__(self, name):
        self.name = name # 인스턴스 변수 생성

person1 = Person('지민')
print(person1.name)
print(person1.blood_color)