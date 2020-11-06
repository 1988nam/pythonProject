# while

n = 5
while n>0:
    print(n)
    n = n-1

#예2

a = ['foo','nar','bar']

while a:
    print(a.pop())

#break continue

n = 5
while n>0:
    n -= 1
    if n == 2:
        break
    print(n)
print('loop end')


m = 5
while m>0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('loop end')

# if 중첩
i = 1

while i <= 10:
    print(i)
    if i == 6:
        break
    i += 1

n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out')

# 예8

a = ['foo','bar','baz']

while True:
    if not a:
        break
    print(a.pop())
