a=[85,76,93,69,87]

answer=[1]*len(a)
for n,i in enumerate(a):
    for j in a:
        if i<j:
            answer[n]+=1
print(answer)
