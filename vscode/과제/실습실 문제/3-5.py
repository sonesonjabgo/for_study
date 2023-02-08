# 받은 값을 튜플로 저장
# 튜플을 한 리스트에 저장
input_list = []
while len(input_list) != 5:
    input_word = input('소금물 농도 소금물의 양: ')
    if input_word == 'Done':
        break
    salt_dense = tuple(map(int, input_word.split()))
    input_list.append(salt_dense)
# 5개 입력하거나 done 입력했을 때 끝내게 하는 코드

# 소금물 농도 공식 : (소금의 양 / 소금물의 양) * 100
saltamount_list = []
saltwater = []
for salt in input_list:
    # salt[0] # 이게 농도
    # salt[1] # 이게 소금물 양
# 소금물 총 합의 소금물 농도를 구해야 함
# 총 소금물의 양과 총 소금의 양이 필요함
# salt[1]을 다 더하면 총 소금물 양
# 농도/100 * 소금물 양 = 소금의 양
# for문으로 소금의 양을 구하고 저장 그리고 소금물 양 저장
    saltamount = salt[0]/100*salt[1]
    saltamount_list.append(saltamount) # 소금 양 저장
    saltwater.append(salt[1])

total_salt = sum(saltamount_list)
total_water = sum(saltwater)

# print((total_salt/total_water)*100)
print(f'혼합된 소금물의 총량은 {total_water}이고, 농도는 {(total_salt/total_water)*100: .2f}입니다.')