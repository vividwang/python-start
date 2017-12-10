sandwichOrders = ['kfc','mcDonald','pizza and more']
finishSandwichs = []

while sandwichOrders:
    currentSandwich = sandwichOrders.pop()
    print("I made your " + currentSandwich)
    finishSandwichs.append(currentSandwich)

for finishSandwich in finishSandwichs:
    print(finishSandwich)