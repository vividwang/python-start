names = ['eric','james','thompson','admin','pake']

for name in names:
    if name == 'admin':
        print('Hello admin,would you like to see a status report.')
    else:
        print('Hello ' + name.title() + ' thank you for logging again.')