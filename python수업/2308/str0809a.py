str1='goodmorning computer'

##for i in 'abcdefghijklmnopqrstuvwxyz':
##    print(f'{i} : {str1.count(i)}')

##for i in range(ord('a'),ord('z')+1):
##    print(f'{chr(i)} : {str1.count(chr(i))}')

str2=list(str1)
print(str2)

str3=set(str1) # 중복없이 요소별로 하나씩만
print(str3)
print(sorted(str3))


for i in sorted(set(str1)):
    print(f'{i} : {str1.count(i)}')
