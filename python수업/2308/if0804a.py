score=int(input("성적 입력 : "))

##if score>=80:
##    print(f'성적 : {score}, 판정 : 합격')
##else:
##    print(f'성적 : {score}, 판정 : 불합격')

##result="합격" if score>=80 else "불합격"
##print(f'성적 : {score}, 판정 : {result}')

# 파이썬 기본 컬렉션(기본 자료형) : 리스트, 딕셔너리,튜플
##score_list=[85,76,93,69,87]
##name_list=['kim','park','choi']
##
##if 'park' in name_list:
##    print('있다')
##else:
##    print('없다')
##
##txt='f'
##if txt in 'Good morning':
##    print(f'Good morning에는 {txt}가 있다.')
##else:
##    print(f'Good morning에는 {txt}가 없다.')

if score>=90:
    print(f'성적 : {score}, 판정 : 수')
elif score>=80:
    print(f'성적 : {score}, 판정 : 우')
elif score>=70:
    print(f'성적 : {score}, 판정 : 미')
elif score>=60:
    print(f'성적 : {score}, 판정 : 양')
else:
    print(f'성적 : {score}, 판정 : 가')
    
