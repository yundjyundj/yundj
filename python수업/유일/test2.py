import random
random.seed(20)

chobap = ['새우', '연어', '장어', '타코와사비', '육회', '광어', '참치', '계란말이', '생새우', '전어']
answer = ''

while True:
    many = int(input('수량입력(10개 이하) : '))
    print(random.sample(chobap,many))
    answer = input("주문을 계속하시겠습니까?")
    if answer=='stop':
        break;
