# a=[1,2,4,7,11,16,22,29,37]

a=[1]
for k in range(1,9):
    a.append(a[k-1]+k)
print(a)
