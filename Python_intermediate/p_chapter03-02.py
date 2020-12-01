# 파이썬 스페셜 메소드 (매직 메소드)
# 파이선의 핵심, 시퀀스(Sequence), 반복(Iterator), 함수(Fuctions), 클래스(Class)
# 클래스안에 정의할 수 있는 특별한(built in) 메소드

# 클래스 예제2
# (5,2) + (4,3) = (9,5)

class Vector(object):
    def __init__(self, *args):
        '''
        Create Vector, example : v = Vectors(5,10)
        '''
        if len(args) == 0:
            self._x, self._y = 0,0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''
        :return: return Vector Method
        '''
        return 'Vector(%r,%r)' % (self._x,self._y)

    def __add__(self, other):
        '''
        :param other:
        :return: return the Vector addtion of self and other
        '''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return (bool(max(self._x,self._y)))

# Vector Instance 생성

v1 = Vector(5,7)
v2 = Vector(23,35)
v3 = Vector()

# 매직 메소드 출력
print(Vector.__init__.__doc__)
print(Vector.__add__.__doc__)
print(Vector.__mul__.__doc__)

print(v1,v2,v3)

print(v1+v2)
print(v1*3)
print(v2*10)
print(bool(v1),bool(v2))

