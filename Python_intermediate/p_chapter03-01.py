# 파이썬 스페셜 메소드 (매직 메소드)
# 파이선의 핵심, 시퀀스(Sequence), 반복(Iterator), 함수(Fuctions), 클래스(Class)
# 클래스안에 정의할 수 있는 특별한(built in) 메소드

# 기본형

print(int(10))
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10

print(n + 100)
print(n.__add__(100))
#print((n.__doc__))
print(n.__bool__(), bool(n))
print(n * 100)
print(n.__mul__(100))

# 클래스 예제1

class Fruit:
    def __init__(self,name,price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info: {}, {}'.format(self._name,self._price)

    def __add__(self,x):
        print('called __add__')
        return self._price + x._price

    def __sub__(self, x):
        return self._price - x._price

    def __le__(self, x):
        print('called le')
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        print('called ge')
        if self._price >= x._price:
            return True
        else:
            return False

# 인스턴스 생성

s1 = Fruit('orange', 7500)
s2 = Fruit('banana', 3000)
print('얍')
print(s1._price + s2._price)
print(s1 + s2)
print(s1._price - s2._price)
print(s1 - s2)

# 매직 메소드
print(s1 <= s2)