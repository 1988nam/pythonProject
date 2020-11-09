# Input
# 기본 타입 str

# 예제 1

# name = input("Enter your name")
# grade = input("Enter your grade")
# company = input("enter your company")

# print(name,grade,company)

# 예 2
'''
number = input("Enter number :")
name = input("Enter name :")

print("type of number", type(number))
print("type of name", type(name))
'''

# 예 3
'''
first_number = int(input("Enter number :"))
second_number = int(input("Enter number :"))

first_number2 = input("Enter number :")
second_number2 = input("Enter number :")

total = first_number + second_number
total2 = first_number2 + second_number2

print(total)
print(total2)
'''

# 예4 (실수형)

float_number = float(input("실수 입력 :"))

print(float_number)
print(type(float_number))

# 예5

print('first name - {0}, Last name - {1}'.format(input('Enter first name'),input('Enter second name')))