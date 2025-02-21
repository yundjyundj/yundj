for i in range(5):
    print(i,end=" : ")
    for j in range(1,6):
        print(f'{i*5+j:3}',end=' ')
    print()

print('='*30)

n=1
for i in range(5):
    for j in range(5-i):
        print(f'{n:3}',end=' ')
        n+=1
    print()
print('='*30)

