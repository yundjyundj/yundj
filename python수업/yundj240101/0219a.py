'''
a=[5,8,9,3]  리스트
b=['excel','word','power']

딕셔너리
짜장면 5000
짬뽕   7000
볶음밥 8000
우동   6000
'''
menu={'짜장면':5000,'짬뽕':7000,'볶음밥':8000,'우동':6000}
print(menu['짜장면'])
print(menu['우동'])
for m in menu:
    print(m)

for m in menu:
    print(menu[m])

order_total=0
order=['짜장면','짜장면','짜장면','짬뽕','볶음밥']
for s in order:
    order_total+=menu[s]
print(f'주문금액 합계 : {order_total}')

'''
a=[5,8,9,3]
a_sum=0
for i in a:
    a_sum+=i
print(a_sum)
'''

student={'홍길동':95,'김기태':80,'서정원':90}
student_total=0 # 합계를 저장할 변수
student_cnt=0   # 인원수를 저장할 변수
for t in student:
    student_total+=student[t]
    student_cnt+=1

print(f'점수 합계 : {student_total}')
print(f'점수 평균 : {student_total/student_cnt}')


