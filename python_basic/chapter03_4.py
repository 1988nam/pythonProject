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


f = dict(
    name = 'niceman',
    city = 'seoul'

    )

print(f)

# dic 출력

#print(f['name1']) # 키 존재 X - 에러발생
print(f.get('name1')) # 키 존재 X - None으로 return
print(f.get(0))

f['address'] = 'busan'
f['rank'] = [1,2,3]
print(f)

#dic_keys ,dic_values,dict_items

print(f.keys()) #key값만 가져오는 함수
print(list(f.keys()))

print(f.values())
print(list(f.values()))
print(f.items())

print(f.pop('name'))
print(f)