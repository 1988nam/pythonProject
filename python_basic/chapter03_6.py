#집합(Set)
#집합(Set) 자료형(순서x, 중복x)

#선언
a = set()
b = set([1,2,3,4])
c = set([1,4,5,6])
d = set([1,2,'pen','cap','plate'])
e = {'foo','bar','bar2'}
f = {42, 'foo',(1,2,3)}

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#튜플변환
print('>>>>')
t = tuple(b)
print(t)
print(type(t))
print(t[0],t[1:3])

#리스트 변환
l = list(c)
l2 = list(e)

print(l)
print(l2)

print(len(a))
print(len(b))
print(len(c))

#집합 자료형 활용

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print('s1 & s2', s1&s2) #교집합
print(s1.intersection(s2))

print('s1 | s2', s1|s2) #합집합
print(s1.union(s2))

print('s1 - s2', s1-s2) #차집합
print(s1.difference(s2))

