score=[85,76,93,69,87]
r=[1 for _ in range(len(score))]

for i in range(len(score)):
    for j in score:
        if score[i]<j: r[i]+=1

print(score)
print(r)

for i in range(len(score)):
    print(f'{score[i]} : {r[i]}')

for i,j in zip(score,r): # [85, 76, 93, 69, 87] [3, 4, 1, 5, 2]
    print(f'{i} : {j}')
