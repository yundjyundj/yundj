str1="goodmorning computer"
number=[8,2,5,4,9]
print(len(str1))
print(len(number))

# str1에서 morning만 출력?
print(str1[4:11])

# str1에서 computer만 출력?
print(str1[12:])

# number에서 [2,5,4] 만 출력?
print(number[1:4])

student=[['홍길동','2005-10-15',90],
         ['선동열','2007-8-2',88],
         ['차두리','2010-5-9',70]]
# 2번째 학생의 이름,생년월일, 성적 출력?
print(student[1])

# 2번째 학생의 생년월일 출력?
print(student[1][1])

# 3번째 학생의 생년월일, 성적 출력?
print(student[2][1:])

# 학생들의 성적만 출력?
for s in student:
    print(s[2])

# 학생들의 성적 합계?
total=0
for s in student:
    total+=s[2]
print(total)
    
# 예) a=[90,88,70]일때 a의 합계
a=[90,88,70]
total=0
for i in a:
    total+=i  # total=total+i
print(total)

