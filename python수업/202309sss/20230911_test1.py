scores=[85,76,93,69,87]
# scores의 모든 요소를 출력
##85
##76
##93
##69
##87
#===========================================
# scores의 모든 요소의 합계(total)를 출력
##1. total에 0을 대입
##2. total=total+첫번째요소
##3. total=total+두번째요소
##4. total=total+세번째요소
##5. total=total+네번째요소
##6. total=total+다섯번째요소
total=0
for i in scores:
    total=total+i  # total+=i
print(total)

# scores의 모든 요소의 합계(total)를 출력
total=0
for i in range(len(scores)):
    total=total+scores[i]  # total += scores[i]
print(total)

