students=[["ydj",85],["sjw",76],["sdy",93],["cjs",69],["sjs",87]]

for k in students:
    if k[1]>=80:
        print(k[0],'의 점수는 ',k[1],'점 합격')
print('-'*30)
for i,j in students:
    if j>=80:
        print(i,'의 점수는 ',j,'점 합격')
