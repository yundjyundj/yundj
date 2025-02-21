'''
a,b,c=10,20,30
total=a+b+c

print('a+b+c=',total)

member=['kim','lee','park','choi']
n1,n2,n3,n4=member

print(n1)
print(n2)
print(n3)
print(n4)

print('-' * 30)
kor=200
mat=300
print(kor,mat)
kor,mat=mat,kor # 값을 바꾼다.
print(kor,mat)
'''

# 국어(kor), 영어(eng), 수학(mat) 3과목의 점수를 입력받아
# 그 합계(total)를 구한다.

kor=int(input("국어 점수 입력 : "))
eng=int(input("영어 점수 입력 : "))
mat=int(input("수학 점수 입력 : "))

total=kor+eng+mat
print(total)
print(type(kor))











