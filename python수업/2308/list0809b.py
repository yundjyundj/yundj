name=["ydj","sjw","sdy","cjs","sjs"]
score=[85,76,93,69,87]
students=[]
for i,j in zip(name,score):
    students.append([i,j])
print(students)

for i,j in enumerate(name,1):
    print(i,j)

for i,j in enumerate(zip(name,score),1):
    print(i,j[0],j[1])
