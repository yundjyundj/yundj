jumin='050315-4123123'
cur_year=2023
if jumin[7]=='1' or jumin[7]=='2' :
    bir_year=int('19'+jumin[0:2])
else:
    bir_year=int('20'+jumin[0:2])
    
age=cur_year - bir_year

if jumin[7]=='1' : sex='남'
elif jumin[7]=='2' : sex='여'
elif jumin[7]=='3' : sex='남'
elif jumin[7]=='4' : sex='여'

# 나이 : 18,  성별 : 여
print(f'나이 : {age},  성별 : {sex}')
