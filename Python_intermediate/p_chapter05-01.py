# 일급 함수 (일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환(return)

# 함수 객체

def factorial(n):
    '''
    Factorail function n : int
    '''
    if n == 1:
        return 1
    return n * factorial(n-1)

class A:
    pass

print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))

print(set(sorted(dir(factorial))) - set(sorted(dir(A))))

print(factorial.__name__)
print(factorial.__code__)

print()
print()

# 변수 할당

var_fuction = factorial

print(var_fuction)
print(var_fuction(10))
print(list(map(var_fuction, range(1,11))))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수
# map, filter, reduce
# es6
print([var_fuction(i) for i in range(1,6) if i % 2]) # 지능형 어쩌고 다시 복습

# reduce

from functools import reduce
from operator import add

print(sum(range(1,11)))
print(reduce(add, range(1,11)))

# 익명함수 (lambda)
# 가급적 주석을 꼭 작성하라
# 일반 함수 형태로 리팩토링을 권장

print(reduce(lambda x, t:x+t, range(1,11)))

print()
print()

# callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인

print(callable(str), callable(A),callable(list), callable(var_fuction), callable(factorial), callable(3.14))

# 3.14 는 상수, -> 상수는 뭐지 ?

# partial 사용법 : 인수 고정 -> 콜백 함수 사용

from operator import mul
from functools import partial

print(mul(10,10))

# 인수 고정

five = partial(mul, 5)
print(five(10))

s = five(7)
print(s)

# 고정 추가

six = partial(five,6)
print(six())

# listcomprehanshion

print([five(i) for i in range (1,11)])

