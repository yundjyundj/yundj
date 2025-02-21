def rank(a):
    r=[1 for _ in range(len(a))]
    for n,i in enumerate(a):
        for j in a:
            if i<j :r[n]+=1
    return r

score=[85,76,93,69,87]
r_score=rank(score)

for i,j in zip(score,r_score):
    print(f'{i} : {j}')


ss=[8,7,6,6,9,5]
r_score=rank(ss)

for i,j in zip(ss,r_score):
    print(f'{i} : {j}')
