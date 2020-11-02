c = [70,75,80,85]
print(c)

temp = c
print(temp,c)
print(id(temp))
print(id(c))

print('>>>>>')
c[0] = 4
print(c)
c[1:2] = [['a','b','c']]
print(c)

print('리스트 체크')
print(c[1])

del c[2] #삭제
print(c)

# 리스트 함수
print('>>>>>')
a = [5,2,3,1,4]
a.append(10)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(a.index(3))
a.insert(2,7)
print(a)
a.reverse()
print(a)

a.remove(10)
print(a)

print(a.pop())
print(a)