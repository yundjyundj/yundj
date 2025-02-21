a=[5,9,2,7,4]
a.append(100)
print(a)     #[5, 9, 2, 7, 4, 100]
a.sort()     #오름차순 정렬
print(a)     #[2, 4, 5, 7, 9, 100]
a.sort(reverse=True)     #내림차순 정렬
print(a)     #[100, 9, 7, 5, 4, 2]
print(a.index(7))   # a라는 리스트에서 7이 몇번째 위치하고 있는지 알려줌

b=[2,3,5,2,3,2,7,2,8,3,9,2]
c='power point'
print(b.count(3)) # b라는 리스트에서 3의 갯수를 구한다.
print(c.count('p')) # c라는 문자열에서 'p'의 갯수를 구한다.
