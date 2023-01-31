words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

in_word_list = []
for word in words_dict:
    if word[0] == 'b' or word[0] == 'm' or word[0] == 'p':
        in_word = 'im' + word
        in_word_list.append(in_word)
    elif word[0] == 'l':
        in_word = 'il' + word
        in_word_list.append(in_word)
    elif word[0] == 'r':
        in_word = 'ir' + word
        in_word_list.append(in_word)
in_word_list.sort(reverse=True)

print(in_word_list)