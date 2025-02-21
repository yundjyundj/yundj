# 1에서 10까지의 합계 구하기
total=0
for i in range(1,11):
    total+=i
print(total)

# 5에서 150000000까지의 정수중 홀수의 합계 구하기
odd_total=0
for i in range(5,150000001):
    if i%2==1:
        odd_total+=i
print(odd_total)
