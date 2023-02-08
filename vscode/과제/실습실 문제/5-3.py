# 입력 예시
s = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'

# 출력 예시
# 'I never dreamed about success, i worked for it.'

s = s.lower()
for str in s:
    if str.isalpha():
        strindex = s.index(str)
        s = s[strindex:]
        break

for str in s[::-1]:
    if str == '.':
        strindex = s.index(str)
        s = s[:strindex+1]
        break
s = s.capitalize()

print(s)