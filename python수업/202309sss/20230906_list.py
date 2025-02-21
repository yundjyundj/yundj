a=[5,2,7,9]
b=['kim','park','yun','Lee','han']

##print(a)
##print(a[0])
##print(b[0])
##print(b[3])
##if 7 in a:
##    print('7은 a안에 있다.')
##else:
##    print('7은 a안에 없다.')
##a=[5,2,7,9]
##b=['kim','park','yun','Lee','han']
### 숫자를 입력받아 그 숫자가 리스트 a안에 있는지 출력한다.
##k=int(input('숫자 입력 : '))
##if k in a:
##    print(f'{k}은 a안에 있다.')
##else:
##    print(f'{k}은 a안에 없다.')

# 1글자를 입력받아 그 값이 아라비아 숫자인지 아닌지를 출력한다.
a=[1,2,3,4,5,6,7,8,9,0]
a=list(map(str,a)) # ['1','2','3','4','5','6','7','8','9','0']
m=input('1글자 입력 : ') 
if m in a:
    print(f'{m}은 숫자이다.')
else:
    print(f'{m}은 숫자아니다.')




