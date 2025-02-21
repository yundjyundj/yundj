a=[85,76,93,69,87]
'''
for i in range(len(a)):
    print(a[i])
'''

for i in a: # a의 모든 요소가 차례로 i에 대입되어 반복문을 처리한다.
    if i>=80:
        print(f"{i} : 합격")
    else:
        print(f"{i} : 불합격")

print("-"*30)
#  a에서 80미만인 숫자만 출력하시오.
for i in a: 
    if i<80:
        print(f"{i}")

print("-"*30)
#  a에서 80이상 90미만인 숫자만 출력하시오.
for i in a: 
    if 80<=i<90:
        print(f"{i}")
    
