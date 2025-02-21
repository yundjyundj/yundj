num=[85,76,93,69,87]

#리스트 num의 모든 요소들의 합계 구하기
total=0
for n in num:
    total=total+n
print(f'num의 총 합계 : {total}')

print('='*30)

# 홀수만 나타내기
for n in num:
    if n%2==1:print(n)
    
length=len(num) # 리스트 num의 요소의 갯수
total=0
for i in range(length):
    total=total+num[i]
print(f'num의 총 합계 : {total}')

print('='*30)



# 리스트 num에서 홀수의 합계 구하기
total=0
for n in num:
    if n%2==1:total=total+n
print(f'num의 홀수 총 합계 : {total}')

# 리스트 num에서 홀수의 갯수 구하기
cnt=0
for i in num:
    if i%2==1:cnt=cnt+1
print(f'num의 홀수 총 갯수 : {cnt}')

# a=[20,30,33,27,40,10]에서 짝수의 합계 구하기
a=[20,30,33,27,40,10]
total=0
for n in a:
    if n%2==0:total=total+n
print(f'a의 짝수 총 합계 : {total}')


















