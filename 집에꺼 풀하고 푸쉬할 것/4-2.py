students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']

students2 = list(set(students))
student_list = []
for student in students2:
    my_tup = (student, students.count(student))
    student_list.append(my_tup)

student_list.sort(key=lambda x:x[1], reverse=True)
print(student_list)
