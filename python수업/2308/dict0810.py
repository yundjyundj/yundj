name=["ydj","sjw","sdy","cjs","sjs",'kkk']
score=[85,76,93,69,87]

student=dict()
for i,j in zip(name,score):
    student[i]=j
print(student)

print('*'*50)

stu=dict(zip(name,score))
print(stu)
