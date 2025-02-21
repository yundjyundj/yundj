# 1에서 10까지의 합계 구하기
##range(10)  => 0 1 2 3 4 5 6 7 8 9
##range(1,10)  => 1 2 3 4 5 6 7 8 9
##range(1,10,2)  => 1 3 5 7 9

##total=0
##for i in range(1,11):
##    print(i,end= ' ')
##    total+=i
##print(total)

# 1에서 10까지의 짝수의 합계 구하기
##total=0
##for i in range(2,11,2):
##    print(i,end= ' ')
##    total+=i
##print(total)

# a에서 b까지의 짝수의 합계 구하기
a,b=map(int,input('2개의 정수 입력 : ').split())

if a>b: a,b=b,a

##total=0
##for i in range(a,b+1):
##    if i%2==0:
##        print(i,end= ' ')
##        total+=i
total=0
while a<=b:
    if a%2==0:
        print(a,end=' ')
        total+=a
    a+=1
print(total)
