f={'사과':1000,'배':1200}
print(f['사과'])
print(f['배'])

# f라는 딕셔너리에 '귤':500 을 추가해보자.
f['귤']=500
print(f)

# 딕셔너리 f에서 '사과'의 값을 1100으로 변경 해보자.
f['사과']=1100
print(f)

# 학생들의 3과목 시험결과
# 홍길동은 [80,90,88] 
# 서정원은 [76,93,87] 
# 선동열은 [85,80,70] 
# 위의 내용을 student라는 딕셔너리로 만드시오.

student={'홍길동':[80,90,88],'서정원':[76,93,87],'선동열':[85,80,70]}
print(student)

for s in student:
    print(f'{s} : {sum(student[s])}')



