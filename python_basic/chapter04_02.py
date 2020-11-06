# 파이썬 반복문
# for

# for in collection
# loop body

for v1 in range(10):
    print('v1 is :', v1)

print()

for v2 in range(1,11):
    print(v2)

print()

for v3 in range(1,11,3):
    print(v3)

# 1 ~ 1000까지의 합을 구하기 for 문으로

sum1 = 0

for v in range(1,1001):
    sum1 += v
print(sum1)

print(sum(range(1,1001)))

# 4의 배수의 합

sum2 = 0
for v1 in range(4,1001,4):
    sum2 += v1
print(sum2)

print(sum(range(4,1001,4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플,집합,사전(딕셔너리)
# Iterables 리턴 함수 : range , reverse, enumerate , filter, map, zip

lotto_number = [11,19,21,28,36,37]
for n in lotto_number:
    print(n)

word = "Beautiful"

for s in word:
    print(s)

# 예4
my_info = {
    'name' : 'lee',
    'age' : 33,
    'city':'seoul'
}

for k in my_info:
    print(k,my_info.get(k))

for v in my_info.items():
    print(v)

# if & for
name = 'PineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

#break
number = [14,3,4,7,10,24,17,2,33,45,15,34,36,38]

for num  in number:
    if num == 34:
        print('found 34')
        break
    else:
        print('not found')

#coutinue

lt = ['1',2,5,True,complex(4)]

for l in lt:
    if type(l) is bool:
        continue
    print(type(l))

# for else

numbers = [14,3,4,7,10,24,17,2,33,45,15,34,36,38]

for num in numbers:
    if num == 49:
        print("found 24")
        break
else:
    print('not found 24')

# 구구단

gugu = 0
for g in range(2,10):
    print(g, "단")
    for g2 in range(1,10):
        print(g,"*",g2,"=",g*g2,end=' / ')
    print()

# 변환 예제

name2 = "aceman"

print(reversed(name2))
print(tuple(reversed(name2)))
print(set(reversed(name2)))