def one(a):
    return a%10

scores=[85,76,93,69,87]
print(sorted(scores))
print(sorted(scores,reverse=True))
print(sorted(scores,key=one))
print(sorted(scores,key=lambda x:x%10))

def odd(a):
    return a%2==0
a=[85,76,93,69,87,80]
result=list(filter(odd,a))
print(result)
