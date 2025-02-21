str1='good morning'
print(str1[0])
print(str1[3])
print(str1[-1])
print(str1[-5])

print(str1[0:4]) #①
print(str1[5:]) #②
print(str1[:]) #③
print(str1[::-1]) #④
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(len(alphabet)) #⑤
print(alphabet[::2]) #⑥

# 주민번호에서 년, 월, 일, 성별 부분을 슬라이싱 해보자
jumin='071209-3123456'

##y : 07
##m : 12
##d : 09
##s : 3

print(str1.count('o'))
print(str1.find('m'))
print(str1.find('o'))
print(str1.find('k'))
print(str1)
print(str1.upper())
print(str1.strip())
print(str1.replace('morning','night'))
print(str1.replace(' ',''))
print(str1.split())
