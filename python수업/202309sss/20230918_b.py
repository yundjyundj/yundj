a=[85,76,93,69,87]

answer=[1]*len(a)
for i in range(len(a)): #0 1 2 3 4
    for j in range(len(a)): #0 1 2 3 4
        if a[i]<a[j]:
            answer[i]+=1
print(answer)
