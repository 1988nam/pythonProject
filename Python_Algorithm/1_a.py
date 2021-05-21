sum=0
for i in range(1,11):
    sum+=i
print(sum)

for i in range(1,10):
    sum = (10+1)*10/2
print(int(sum))

i = 1
while i <=3:
    print(i," Hello world")
    i+=1
print("while문 종료")

for i in range(0,3):
    print(i)
    if i ==2:
        break

for i in range(1,19):
    if i > 5:
        continue
    print(i)