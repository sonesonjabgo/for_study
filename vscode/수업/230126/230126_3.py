original_list = [1, 2, 3]
copy_list = original_list
print(original_list, copy_list)

copy_list[0] = 'hello'
print(original_list, copy_list)
# 대입 연산자 (=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사
