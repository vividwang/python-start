favoriteLanguages = {
    'jen':'C',
    'sarah':'Python',
    'edward':'ruby',
    'phil':'Python',
}

queryer = ['Jamme','sarah','phil']

for name in favoriteLanguages.keys():
    if name in queryer:
        print(name + ",thank you!")
    else:
        print(name + ",we invites you to join us!")