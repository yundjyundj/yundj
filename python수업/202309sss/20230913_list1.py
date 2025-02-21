##c = ['Life', 'is', 'too', 'short']
##print(c[0])
##print(c[0][2])
##print(c[2])
##
##e = [1, 2, ['Life', 'is']]
##print(e[2])
##print(e[2][0])
##print(e[2][0][1])

a=list(range(1,10,2))
print(a)
a.append(99)
print(a)   #[1, 3, 5, 7, 9, 99]
a[2]=100
print(a)   #[1, 3, 100, 7, 9, 99]
del a[2]
print(a)   #[1, 3, 7, 9, 99]


