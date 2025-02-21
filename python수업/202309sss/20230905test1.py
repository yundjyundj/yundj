##a=10
##a+=1 # a=a+1
##print(a)

##a=30
##b=50
##print(a,b)  # 30 50
##
###문제
##a,b=b,a
##print(a,b)  # 50 30

#2개의 정수를 키보드로 입력받아 덧셈하여 출력
##num1=int(input('숫자 입력 : '))
##num2=int(input('숫자 입력 : '))
##print(num1+num2)

#이름,국어,영어,수학 점수를 입력받아 홍길동 85 73 69 227 처럼 나타나도록
##name=input('이름 입력 : ')
##kor=int(input('국어 점수 입력 : '))
##eng=int(input('영어 점수 입력 : '))
##mat=int(input('수학 점수 입력 : '))
##total=kor+eng+mat
##
##print(name,kor,eng,mat,total)
##print('%s의 점수 합계는 %d이다' %(name,total))
##print('{}의 점수 합계는 {}이다'.format(name,kor+eng+mat))
##print(f'{name}의 점수 합계는 {kor+eng+mat}이다')

##print('홍길동 : ',sep='',end='')
##print(100)

##name='홍길동'
##score=89
##grade='우'
### 홍길동의 점수 : 89 , 등급 : 우


# 이름과 점수를 입력받아 "홍길동 : 합격(85)" 형식으로 출력
score=85
if score>=80 :
    pass
else:
    result='불합격'

print('end')

