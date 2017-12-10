def buildProfile(first,last,**userInfo):
    userInfo['firstName'] = first
    userInfo['lastName'] = last
    return userInfo

user = buildProfile('w','b',location="HeFei",field='computer',like='music')
for info in user.items():
    print(info)