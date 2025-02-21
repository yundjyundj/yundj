students=[['홍길동','2005-10-15',90],
         ['선동열','2007-8-2',88],
         ['차두리','2010-5-9',70],
         ['김길동','2008-10-15',93],
         ['박동열','2009-8-2',85],
         ['김두리','2006-5-9',79]]
# ['이름','생년월일',성적]
#students에서 성적이 80이상인 학생 수?
s_cnt=0
for s in students:
    if s[2]>=80:s_cnt+=1
print(f'성적이 80이상인 학생 수 : {s_cnt}')

#students에서 성적이 80이상인 학생들의 이름?
s_names=[]
for s in students:
    if s[2]>=80:s_names.append(s[0])
print(f'성적이 80이상인 학생 이름 : {s_names}')

#students에서 김씨성을 가진 학생 수?
s_kim=0
for s in students:
    if s[0][0]=='김':s_kim+=1
print(f'김씨성을 가진 학생 수 : {s_kim}')

#students에서 김씨성을 가진 학생 이름?
s_kim_names=[]
for s in students:
    if s[0][0]=='김':s_kim_names.append(s[0])
print(f'김씨성을 가진 학생 이름 : {s_kim_names}')

#students에서 15세 이상 학생의 이름? 
s_names15=[]
for s in students:
    if int(s[1][0:4])<2010:s_names15.append(s[0])
print(f'15세 이상 학생의 이름 : {s_names15}')
