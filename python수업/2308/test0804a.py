a=int(input("정수 입력 : "))
b=int(input("정수 입력 : "))

print(f'a={a}, b={b}')   # a=20, b=5
print(f'a + b = {a+b}') # 덧셈
print(f'a - b = {a-b}') # 뺄셈
print(f'a * b = {a*b}') # 곱셈
print(f'a / b = {a/b:.1f}') # 나눗셈  d(10진정수), f(실수)
print(f'a // b = {a//b}') # 몫
print(f'a % b = {a%b}') # 나머지
print(f'a ** b = {a**b}') # 제곱근

print('a = %d, b = %d' %(a,b))
print('a={}, b={}'.format(a,b))
