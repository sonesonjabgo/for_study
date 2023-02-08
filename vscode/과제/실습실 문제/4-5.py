test_status = {
    '김싸피': 'solving',
   	'이코딩': 'solving',
   	'최이썬': 'cheating',
   	'오디비': 'sleeping',
   	'임온실': 'cheating',
   	'조실습': 'solving',
   	'박장고': 'sleeping',
   	'염자바': 'cheating'
}
cheat_list = []
for name in list(test_status.keys()):
    if test_status[name] == 'cheating':
        cheat_list.append(name)
        test_status.pop(name)
    elif test_status[name] == 'sleeping':
        test_status[name] = 'solving'

cheat_list.sort()
print(cheat_list)
print(f'test_status = {test_status}')