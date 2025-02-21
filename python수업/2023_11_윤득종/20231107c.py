# 이름입력 :
# 국어입력 :
# 영어입력 :
# 수학입력 :
# 위 처럼 입력받아
# 홍길동의 점수 평균은 85점 이다
# 위 형태의 결과가 나오도록 코딩해보자

name=input('이름입력 : ')
kor=int(input('국어입력 : '))
eng=int(input('영어입력 : '))
mat=int(input('수학입력 : '))

print(f'{name}의 점수 평균은 {round((kor+eng+mat)/3,1)}점 이다.')
print(f'{}의 점수 평균은 {}점 이다')
