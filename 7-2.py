askQuestion = 'You see,I have to know'
askQuestion += '\nHow many people wanna have dinner?'
howManyPeople = input(askQuestion)

if int(howManyPeople) > 8:
    print("There is no empty to eat!")
else:
    print("It's all right to have dinner!")