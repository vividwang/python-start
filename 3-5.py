inviters = ['Lordy','Glory','Flandre','Sand']

pop_inviter = inviters.pop()
print(pop_inviter.title() + " can't be here tonight.")
inviters.append('Ada')

for item in inviters:
    print('Welcome to join dinner, ' + item.title() + '.')