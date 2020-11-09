# 파이썬 클래스
# OOP (객체 지향 프로그래밍), self 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이
# 클래스 - 붕어빵틀 / 인스턴스 - 코드에서 사용하는 객체
#

# 예1

class Dog2: # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self,name,age):
        self.name = name
        self.age = age

#클래스 정보

print(Dog2)

# 인스턴스화

a = Dog2('mikky',2)
b = Dog2('baby',3)

# 비교

print(a==b,id(a),id(b))

# 네임스페이스

print('dog1',a.__dict__)
print('dog1',b.__dict__)

# 인스턴스 속성 확인

if a.species == 'firstdog':
    print('{} is a {}'.format(a.name,a.species))
    print('{0} is a {1}'.format(a.name, a.species))

# 예2
# self의 이해
# 이거 모르겠다. () 들어가면 클래스 메소드 / (self) 들어가면 인스턴트 메소드 인데
# 클래스 인스턴스 객체에 대해서 좀 더 공부 필요

class SelfTest:
    def func1():
        print('Func1 called')
    def func2(self):
        print(id(self))
        print('Func2 called')

f = SelfTest


SelfTest.func1()


# 예3
# 클래스 변수 / 인스턴스 변수
# 클래스 - 모두가 공유하는 / 인스턴스 - 나만 사용하는

class Warehouse:
    # 클래스 변수 = 0
    stock_num = 0

    def __init__(self,name):    #생성자
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):          #소멸자
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
#Warehouse.stock_num = 50

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)

# 인스턴스 > 클래스 > 클래스에도 없으면 에러 남

del user1
print(Warehouse.__dict__)

# 예제4

class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def info(self):#메소드
        return '{} is {} years old'.format(self.name,self.age)

    def speak(self,sound):
        return '{} says {}!'.format(self.name,sound)

# 인스턴스 생성

c = Dog('july',4,)


print(c.info())
print(c.speak('wal wal'))

# 맨 마지막 것 이해 못 했음. why ???
