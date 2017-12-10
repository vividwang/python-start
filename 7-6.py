age = ''
while age != 'quit':
    age = input('How old are ya?')
    if age == 'quit':
        break
    if int(age) < 3:
        print('You are for free.')
    elif int(age) > 3 and int(age) < 12:
        print('You have to pay 10 dollers.')
    else:
        print('You have to pay 15 dollers.')