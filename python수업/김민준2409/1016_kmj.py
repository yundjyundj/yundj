# 대입연산자 =
# 오른쪽의 내용을 왼쪽에 넣어라
'''
a=int(input("a값 입력 : "))
b=int(input("b값 입력 : "))
c=a+b
print(f'{a}+{b}={c}')
'''
# 시작값 : 
# 종료값 :
# 시작값 부터 종료값 사이의 모든 수의 합계

total=0
s=int(input("시작값 입력 : "))
e=int(input("종료값 입력 : "))
for i in range(s,e+1):
    total=total+i
print(f'{s}부터 {e}까지의 합계 : {total}')
