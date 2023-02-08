class Doggy:
    num_of_dogs = 0  # 클래스 변수 선언
    birth_of_dogs = 0

    def __init__(self, name, type):
        self.name = name  # 인스턴스 변수 
        self.type = type  # 인스턴스 변수
        Doggy.num_of_dogs += 1  
        Doggy.birth_of_dogs += 1
        # 생성자 함수 init이 실행될 때 클래스 변수의 숫자를 하나 올린다

    def bark(self):
        print(f'{self.name}(이)가 짖습니다. 월월월')

    def death(self):
        deaddog = input('name : ')
        if deaddog == self.name:
            Doggy.num_of_dogs -= 1

    @classmethod
    def get_status(cls):
        print(cls.birth_of_dogs, cls.num_of_dogs)


robert = Doggy('robert', 'Jindo')
cute = Doggy('cute', 'human')

print(robert.name, robert.type)
robert.bark()
cute.death()
Doggy.get_status()