# 2개의 정수를 키보드로 입력받아
# 각각 a와 b에 저장하고 그 합계를 구해보자.
# 출력 예
# a=
# b=
# 10 + 20 = 30
'''
a=int(input("a="))
b=int(input("b="))

print(f"{a}+{b}={a+b}")
'''
'''
# score라는 리스트에 5개의 성적을 키보드로 입력하기
score=[]
for i in range(5):
    n=int(input("성적입력 : "))
    score.append(n)

print(score)
'''
# score라는 리스트에 5개의 성적을 키보드로 입력하고
# 그 합계를 구하는 프로그램 작성
score=[]
total=0
for i in range(5):
    n=int(input("성적입력 : "))
    total=total+n
    score.append(n)
    

print(score)
print(total)







