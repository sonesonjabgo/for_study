# 캡슐화 getter setter 메서드
class Person:
    def __init__(self, age):
        self.__age = age

    @property # 변수의 값을 읽는 메서드
    def age(self):
        print('getter 호출 !')
        return self.__age

    @age.setter # 변수의 값을 설정하는 성격의 메서드
    def age(self, age):
        if age <= 19:
            raise ValueError('너무 어린데')
        else:
            self.__age = age

    # age = property(get_age, set_age)

kimssafy = Person(20)
print(f'kimssafy는 {kimssafy.__age}')