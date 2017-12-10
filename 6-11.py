cities = {
    'London':{
        'country':'England',
        'population':12000000,
        'fact':'enconomy',
    },
    'Paris':{
        'country':'French',
        'population':10000000,
        'fact':'art',
    },
    'ShangHai':{
        'country':'China',
        'population':25000000,
        'fact':'beauty',
    },
}

for city,cityInfo in cities.items():
    print(city + ':' + cityInfo['country'] + ' '
          + str(cityInfo['population']) + ' ' +
          cityInfo['fact'])