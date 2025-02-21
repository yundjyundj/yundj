a=input('숫자 입력 : ').split() # 한줄에 입력된 여러 숫자를 공백으로 분리

a=list(map(int,a))
# map(함수명,리스트)  리스트 각 요소를 함수에 적용
print(a)
