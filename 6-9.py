favorite_places = {
    'Parry':{
        'lovedPlace':{
            'New york',
            'London',
        }
    },
    'Lorde':{
        'lovedPlace':{
            'BeiJing',
            'London',
            'ShangHai'
        }
    },
    'Jefe':{
        'lovedPlace':{
            'Los Angeles',
        }
    }
}

for user,lovedPlace in favorite_places.items():
    print(user + ':' + "favorite place was " + str(lovedPlace['lovedPlace']))