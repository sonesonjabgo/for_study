password1 = 'password'
chance = 0
while chance < 3:
    password2 = input('비밀번호를 입력하세요. : ')
    chance += 1
    if password1 == password2:
        print('옳은 비밀번호 입니다.')
        break
    else:
        print('틀린 비밀번호 입니다.')
        