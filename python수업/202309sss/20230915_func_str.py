def str_count(str1):
    answer=[]
    cnt=set(str1)
    #cnt=['a','b','c','d']
    for i in cnt:
        answer.append([i,str1.count(i)])
    return answer

str1='abcdabcabdabadaa'
ret=str_count(str1)
print(ret)
