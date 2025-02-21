def rank(a):
    answer=[1]*len(a)
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i]<a[j]:
                answer[i]+=1
    return answer
def mx_func(a):
    mx=0
    for i in range(len(a)):
        if mx<a[i]:
            mx=a[i]
    return mx
def mn_func(a):
    mn=100
    for i in range(len(a)):
        if mn>a[i]:
            mn=a[i]
    return mn

a=[85,76,93,69,87]
##print(rank(a))
b=[67,98,78,80,82,69,79,88,95]
##print(rank(b))
##print(mx_func(a))
##print(mx_func(b))
print(mn_func(a))
print(mn_func(b))





