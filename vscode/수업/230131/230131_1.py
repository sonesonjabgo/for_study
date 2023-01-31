# # 데코레이터 연습
# def ko_hello(name):
#     print(f'안녕하세요, {name}님')

# def en_hello(name):
#     print(f'Hello, {name}!')

# def add_emoji(name, func):
#     func(name)
#     print('^~^//')

# def emoji_decorator(func):
#     def wrapper(name):
#         func(name)
#         print('^~^//')

#     return wrapper

# (emoji_decorator(ko_hello))('재형')
# # (wrapper)('재형')
# # emoji_decorator(en_hello)('재형')

# def emoji_decorator(func):
#     def wrapper(name):
#         func(name)
#         print('^~^//')

#     return wrapper

# @add_tears # 오후에 해보기
# @emoji_decorator  # 이 코드 한 줄로 인해 위의 함수를 편하게 사용할 수 있다
# def ko_hello(name):
#     print(f'안녕하세요, {name}님')

# ko_hello('재형')


class MyClass:
    
    def method(self):
        return 'instance method'

    @classmethod
    def classmethod(cls):
        return 'class method'

    @staticmethod
    def staticmethod():
        return 'static method'

my_class = MyClass()
print(my_class.method())
print(my_class.classmethod())
print(my_class.staticmethod())
