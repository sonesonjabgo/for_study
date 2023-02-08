entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']


# # entry_record를 세트로 변환해서 무슨 요소들이 있는 지 확인하고
# # 그것들의 개수를 리스트의 함수인 count로 센 다음 
# # 요소의 이름과 개수를 딕셔너리로 저장

# entry_set = set(entry_record)
# # {'안도둑', '박장고', '염자바', '최이썬', '이싸피', '임온실', '오디비', '조실습'}
# # for문을 사용해서 순회하려면 iterable인 리스트로 바꿔야 함
# entry_list = list(entry_set)
# count_list = []
# for name in entry_list:
#     count_list.append(entry_record.count(name))

# name_zip = list(zip(entry_list, count_list))
# name_zip.sort(key=lambda x: x[1], reverse=-1)

# print('입장 기록 많은 Top3')
# print(f'{name_zip[0][0]} {name_zip[0][1]}회')
# print(f'{name_zip[1][0]} {name_zip[1][1]}회')
# print(f'{name_zip[2][0]} {name_zip[2][1]}회')

# # 출입 기록 부분
# # if 사용해서 입장 횟수 - 퇴장 횟수 값 판단
# # 사람 당 횟수 찾아야 함 count 사용
# # 위에 name_zip에 사람당 입장 횟수 묶음 있음
# # 확실하게 하려면 따로 해야 함 입장엔 있고 퇴장엔 없을 수 있음
# exit_set_list = list(set(exit_record))
# exit_count = []
# for name in exit_set_list:
#     exit_count.append(exit_record.count(name))

# name_zip2 = list(zip(exit_set_list, exit_count))
# name_zip2.sort(key=lambda x: x[1], reverse=-1)

# dict1 = dict(name_zip)
# dict2 = dict(name_zip2)

# print(dict1[])

from collections import Counter

entryrank = Counter(entry_record).most_common(3)
print('입장 기록 많은 Top3')
print(f'{entryrank[0][0]} {entryrank[0][1]}회')
print(f'{entryrank[1][0]} {entryrank[1][1]}회')
print(f'{entryrank[2][0]} {entryrank[2][1]}회')

entry = Counter(entry_record)
exit = Counter(exit_record)

inminusout = (entry - exit).most_common()
outminusin = (exit - entry).most_common()
# print(inminusout)
# print(outminusin)

print('\n출입 기록이 수상한 사람')
for i in inminusout:
    print(f'{i[0]}은 입장 기록이 {i[1]}회 더 많아 수상합니다.')
for i in outminusin:
    print(f'{i[0]}은 퇴장 기록이 {i[1]}회 더 많아 수상합니다.')