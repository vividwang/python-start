sandwichOrders = ['kfc','pastrami','pastrami','mcDonald','pastrami','pastrami','pizza and more']
finishSandwichs = []

print("We have sold out all the pastrami.")
while 'pastrami' in sandwichOrders:
    sandwichOrders.remove('pastrami')

finishSandwichs = sandwichOrders
for finishSandwich in finishSandwichs:
    print(finishSandwich)