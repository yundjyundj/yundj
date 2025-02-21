a=[5,7,9,2,8]
b='python'

##for i in a:
##    print(i)
##
##for s in b:
##    print(s)

# range(5) 는 0,1,2,3,4 이다.
# range(1,5) 는 1,2,3,4 이다.
# range(1,5,2) 는 1,3 이다.

for i in range(len(a)):  # range(5) 는 0,1,2,3,4 이다.
    print(i,a[i])

for s in range(len(b)):
    print(s,b[s])
