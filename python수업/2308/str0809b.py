str1='goodmorning'

str2=str1.replace('morning','night')
print(str2)


numbers='50 70 30'
a,b,c=numbers.split()
print(a,b,c)
print(a+b+c)

numbers='50 70 30'
a,b,c=map(int,numbers.split()) #map(함수명,반복자료형) : 반복자료가 하나씩 모두 함수의 적용을 받는다.
print(a,b,c)
print(a+b+c)
