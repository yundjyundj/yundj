# a와 b값을 입력받아 a에서 b까지의 합계 구하기
a=int(input('a값 입력 : '))
b=int(input('b값 입력 : '))

s=0
for i in range(a,b+1):
    s=s+i
print(f'a에서 b까지의 합계 : {s}')


t=(a+b)*(b-a+1)/2
print(f'a에서 b까지의 합계 : {t}')

