str_lst = input('문자열을 입력하세요. : ')
str_lst = list(str_lst.lower().split())
print(str_lst)

# 리스트 첫 번째 문자열 마지막 글자
# str_lst[0][-1]
# str_lst[1][0] 이랑 같아야 함

# if str_lst[i][-1] == str_lst[i+1][0]:
#     print('Pass')
# else:
#     print('Fail')

for i in range(len(str_lst)-1): # 마지막거 비교하는거 제외해야 함
    
    if str_lst[i][-1] != str_lst[i+1][0]: 
        print('Fail')
        break
else:
    print('Pass')