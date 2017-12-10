people = {
    'friend1' : {
        'firstname':'Jane',
        'lastname':'Andson',
        'age':22,
        'city':'New York',
    },
    'friend2' : {
        'firstname':'Jane',
        'lastname':'Andson',
        'age':22,
        'city':'New York',
    },
    'friend3' : {
        'firstname':'Jane',
        'lastname':'Andson',
        'age':22,
        'city':'New York',
    },
}

for user,userInfo in people.items():
    print(user + ':' + userInfo['firstname'],userInfo['lastname'],userInfo['age'],userInfo['city'])