number=[85,76,93,69,87]
'''
print(number)
print(number[0]) # 첫번째 요소
print(number[1:3]) # 1에서 2번까지
print(number[-1]) # 마지막 요소

for n in number: # number의 각 요소가 n에 대입되어 반복문을 처리한다.
    print(n+100)
'''

for n in number:
    if n>=80:
        print(f'{n} : 합격')
    else:
        print(f'{n} : 불합격')

print('='*30)

for n in number:
    if n>=90:print(f'{n} : 수')
    elif n>=80:print(f'{n} : 우')
    elif n>=70:print(f'{n} : 미')
    elif n>=60:print(f'{n} : 양')
    else:print(f'{n} : 가')

'''
문제 :
a=[6,8,2,1,9,5]의 각 요소에 10을 더하여 출력
16
18
12
11
19
15
'''





