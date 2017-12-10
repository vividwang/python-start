pets = {
    'lary':{
        'type':'dog',
        'master':'Henrry',
    },
    'ray':{
        'type':'dog',
        'master':'dave',
    },
    'sarah':{
        'type':'cat',
        'master':'Kevin',
    },
}

for pet,petInfo in pets.items():
    print(pet + ':' + petInfo['type'] + petInfo['master'])