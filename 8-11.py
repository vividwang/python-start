magicians = ['David','Louis','Jerry','Ken','Poton']

def makeGreat(people):
    for value in range(0,len(people)):
        oldValue = people[value]
        people[value] = "The Great " + oldValue
    showMagicians(people)

def showMagicians(people):
    for person in people:
        print(person)

makeGreat(magicians[:])
showMagicians(magicians[:])