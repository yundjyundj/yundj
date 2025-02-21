def odd_hap(num_list):
    total=0
    for i in num_list:
        if i%2==1:
            total+=i
    return total

a=[8,9,4,2,5,1,7]
ret=odd_hap(a)
print(ret)

b=[22,25,21,17,19,34,35,31]
ret=odd_hap(b)
print(ret)

def list_hap(num_list):
    total1=total2=0
    for i in num_list:
        if i%2==1:
            total1+=i
        else:
            total2+=i
    return total1,total2


a=[8,9,4,2,5,1,7]
ret=list_hap(a)
print(ret)

b=[22,25,21,17,19,34,35,31]
ret=list_hap(b)
print(ret)
