#파이썬 튜플
#튜플 자료형(순서o ,중복o ,수정 삭제 x)

#선언

a = ()
b = (1,2)
c = (11,12,13,14)
d = (100,1000, 'Ace','Base','Captine')
e = (100,1000, ('Ace','Base','Captine'))

#인덱싱

print ('>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))


#수정x
#d[0] = 1500

#슬라이싱
print ('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', d[2:])

#튜플 연산
print ('>>>>>')
print (c+d)
print (c*3)

#튜플 함수
