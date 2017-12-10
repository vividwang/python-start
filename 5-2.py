#更多的条件测试
car = 'Audi'
print(car == 'audi')
print(car != 'audi')
print(car.lower() == 'audi')
number1 = 20
number2 = 22
if number1 == number2:
    print('Number1 equals number2')
elif number1 >= number2:
    print('Number1 >= number2')
elif number1 <= number2:
    print('Number1 <= number2')

if number1 > 20 and number2 > 20:
    print('Numebr1 and number2 great than 20')
elif number1 < 20 and number2 < 20:
    print("Numebr1 and number2 less than 20")
elif number1 >= 20 or number2 <= 30:
    print('Number1 great than 20 or number2 less than 30')

myList = ['Hello','World']
print('Hello' in  myList)
print('what' not in myList)
