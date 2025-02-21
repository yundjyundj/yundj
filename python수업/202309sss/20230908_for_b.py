a='good morning'
# 위의 a에서 morning만 출력하자.

##for i in a:
##    print(i)

office = ['word', 'excel', 'powerpoint','access']
##for app in office:
##    print(app)
##
##for i in range(len(office)):
##    print(office[i])

# office의 요소들을  글자수-내용 형식으로 출력  4-word
for s in office:
    print(f'{len(s)}-{s}')
    


