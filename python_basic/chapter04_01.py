# 파이썬 제어문
# IF 실습

# 기본 형식
print(type(True)) # 0이 아닌 수,
print(type(False)) # 0 ,"",[],(),{}...

# 예1

if True:
    print('good')

if False:
    print('Bad')

# 예2
print('예2')
if True:
    print('Bad')
else:
    print('good')

print()
# 관계연산자
# > >= < <= == !=
x = 15
y = 10

print(x==y)
print(x != y)

print(x > y)
print(x >= y)
print(x < y)
print(x <= y)

print()

#예3
city =""
if city:
    print('you are in:',city)
else:
    print('please enter your city')

#예4
city2 ="Seoul"
if city2:
    print('you are in:',city2)
else:
    print('please enter your city')

#논리연산자
# and or not

a = 75
b = 40
c = 10

print('and :',a > b and b > c)

print(not True)
print(not False)

# 산술,관계,논리 우선순위
# 산술 > 관계 > 논리

print('e1', 3+12 > 7+3)
print('e2', 5+10*3 >7+3*20)
print('e3',5+10 >3 and 7+3 ==10)
print('e4',5+10>0 and not 7+3==10)

score1 = 100
score2 ='b'

#예4
if score1 >= 90 and score2 =='a':
    print('pass')
else:
    print('Fail')

#예5

id1 = 'vip'
id2 = 'admin'
grade ='platinum'

if id1 == 'vip' or id2 =='admin':
    print('관리자')

if id2 == 'admin' and grade =='platinum':
    print('슈퍼관리자')

#예6
#다중조건문

num = 50
if num >= 90:
    print('Grade A')
elif num >= 80:
    print('Grade B')
elif num >= 70:
    print('Grade C')
else:
    print('과락')

#중첩조건문

grade = 'A'
total = 0

if grade =='A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 50%')
    else:
        print('장학금 30%')
else:
    print('장학금 X')

# in, not in
# 리스트 / 집합 / 딕셔너리 / 튜플
q = [10,20,30]
w = {70,80,90,100}
e = {"name": "lee", "city": "seoul", "grade":"a"}
r = (10,12,14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)