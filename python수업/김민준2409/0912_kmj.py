a="computer"
b=len(a) # a의 글자수를 b에 대입한다.

# range(5) : 0,1,2,3,4를 의미한다.
'''
for i in range(5):
    print(i)

for i in range(0,5,2):
    print(i)

# 0 2 4 6 8 10 이 출력 되도록 작성하시오.
for i in range(0,11,2):
    print(i)

for i in range(b):
    print(a[i])
'''
#computer를 retupmoc처럼 거꾸로 출력해 보자.
for i in range(b-1,-1,-1):
    print(a[i])
    
# 아래의 문자열에서 3의배수만 출력
n="123456789"
for i in range(2,len(n),3):
    print(n[i])
    
