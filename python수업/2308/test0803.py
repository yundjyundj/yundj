##a=10
##b=20
##c=a+b
##print("a + b =",c)
##
##a="good"
##b="morning"
##c=50
##d=100
##print(a+b) # 데이터형식이같으면 +, * 가능
##print(c+d)
###print(b+c) # error
##print(b,c)
##
### 문자열을 정수로 : int
### 정수를 문자열로 : str
##print(b + str(c))


# 키보드로 값을 입력 받을때 : input
##a=int(input("첫번째 수 입력 : "))
##b=int(input("두번째 수 입력 : "))
##a,b=30,60
##print("a + b = ",a+b)
##print(a,b)
##a,b=b,a
##print(a,b)

# split() : 공백문자를 기준으로 문자열을 분리해줌
a,b=input("2개의 정수 입력 : ").split()

print(a,b)
print(int(a)+int(b))
















