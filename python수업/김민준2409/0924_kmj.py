a=[53,60,42,97,31,80,77]

for i in a:
    print(i)
# a의 요소 53,60,42,97,31,80,77이 차례로 i에 대입하여
# print(i) 명령을 반복 처리한다.

print("-"*30)

total=0
for i in a:
    total=total+i # total에 i값을 누적 시킨다.
# a의 요소 53,60,42,97,31,80,77이 차례로 i에 대입하여
# total=total+i 명령을 반복 처리한다.
# 즉 a의 모든 요소의 합을 total에 저장하게된다.
print(f"총합계 : {total}")
print("-"*30)

cnt=0
for i in a:
    cnt=cnt+1
# a의 요소를 i로 하나씩 넘겨 받을때마다 cnt값을 1 증가 시킨다.
print(f"총갯수 : {cnt}")
print("-"*30)
#====================================================
total=0
for i in a:
    if i>=80:
        total=total+i # i가 80이상일 경우만 total에 i값을 누적 시킨다.

print(f"80 이상 합계 : {total}")
print("-"*30)

cnt=0
for i in a:
    cnt=cnt+1
# i가 80이상일 경우만 cnt에 1을 증가 시킨다.
print(f"총갯수 : {cnt}")
print("-"*30)
