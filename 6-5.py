rivers ={
    'nile':'egypt',
    'yongtz river':'china',
    'yellow river':'china',
}

for key,value in rivers.items():
    print("The " + key.title() + " runs though " + value.title())

print('The following river have been mentioned:')
for key in rivers.keys():
    print(key)

print('The following country have been mentioned:')
for value in rivers.values():
    print(value)