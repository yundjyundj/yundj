import random
random.seed(20)
students = ['찬민', '한주', '담도', '성민', '용윤', '레이', '우상', '노윤', '웅준', '윤서', '인서', '한승', '사비', '원재', '윤하', '현서', '연지', '하주', '윤지', '서현', '은예', '예지', '정현', '진현', ]
red = random.sample(students,12)
k=['찬민', '한주', '담도']
for i in red:
    students.remove(i)
##for i in red:
##    if i in students:
##        students.remove(i)
blue=students
print(red)
##print(len(red))
print(blue)
print(students)

print(dir(list))
