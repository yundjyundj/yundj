a=[85,76,93,69,87]
print(a[2]) # 인덱싱   리스트이름[인덱스번호]

student={'name':'Yun','class':3,'score':[85,76,93],1:(1,2,3)}
print(student['name'])  # dict의 인덱싱은 dict이름[key]
print(student['class'])
print(student['score'])
print(student[1])

#아래의 dict는 이름:[국어,영어,수학] 형태로 key와 value가 구성되어있다.
student={'hgd':[90,87,85],'sjw':[80,90,70],'ydj':[85,95,90]}
# 'sjw'의 영어 점수 출력
print(student['sjw'][1])
# 'ydj'의 3과목 점수 합계 출력
# a=[50,60,70] 에서 a의 합계는 sum(a) 이다.
print(sum(student['ydj']))

for s in student:
    # dict를 for로 반복하면 dict의 key들이 차례로 s에 대입되어 처리된다.
    print(student[s])

# hgd : 262
# sjw : 240
# ydj : 270

for s in student:
    print(f'{s} : {sum(student[s])}')

print(student) # {'hgd': [90, 87, 85], 'sjw': [80, 90, 70], 'ydj': [85, 95, 90]}
student['sjw']=[10,10,10]
print(student)
student['cdw']=[60,70,80]
print(student)
del student['sjw']
print(student)

print('-'*30)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
