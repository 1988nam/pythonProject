# 함수식 및 람다

# 함수 정의 방법
# def function_name
#   code

# 예1

def first_func(w):
    print('hello',w)

word = 'nam'

first_func(word)

# 예2

def return_func(w1):
    return 'Hello ' + str(w1)

x = return_func('goodboy2')
print(x)

# 예3 다중반환

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1,y2,y3

x,y,z = func_mul(10)
print(x,y,z)

# 튜플 리턴

def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1,y2,y3)

q = func_mul2(20)
print(type(q),list(q))

# 튜플 () 리스트[] 딕셔너리{} 이걸 왜 알아야 하나 ? 어디서 써먹지 ??
# Dic 은 key 가 있어야 한다.?


# 중요
# *args , **kwargs
# 팩킹 , 언팩킹

# *args(언팩킹) 튜플

def args_func(*args): #매개변수 명 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i),v)
    print('------')

args_func('Lee','Park')
args_func('Lee','Park','Kim')

# **kwargs (언팩킹) 딕셔너리

def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print('{}'.format(v),kwargs[v])
    print('------')

kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Joe')

# 전체 혼합

def example(args_1,args_2,*args,**kwargs):
    print(args_1,args_2,args,kwargs)

example(10,20,'Lee','Kim','Park', age1=20,age2=30,age3=40)

# 중첩 함수

def nested_func(num):
    def func_in_func(num):
        print(num)
    print('In func')
    func_in_func(num + 100)

nested_func(100)

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수 (Heap 초기화) -> 메모리 초기화


#def mul_func(x,y):
#    return x * y

#a = lambda x,y:x*y
#a(5,6)

def mul_func(x,y):
    return x * y

q = mul_func(10,50)
print(q)

print(mul_func(10,50))

lambda_mul_func = lambda x,y:x*y

print('lamda')
print(lambda_mul_func(10,50))

