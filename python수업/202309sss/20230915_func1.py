def hap(a,b): # 함수이름(hap)과 매개변수(a,b)
    c=a+b
    return c # 함수를 호출한 곳으로 c값을 반환(return)한다.

def cal(a,b): # 함수이름(hap)과 매개변수(a,b)
    c=a+b
    d=a*b
    return c,d # 함수를 호출한 곳으로 c와 d값을 반환(return)한다.

num1=80
num2=70
ret1=hap(num1,num2) # num1과 num2를 매개변수에 전달하면서 함수호출.
ret2=hap(50,60)
print(ret1)
print(ret2)

ret3=cal(num1,num2)
print(ret3)
ret4,ret5=cal(num1,num2)
print(ret4,ret5)
