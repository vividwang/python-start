def makeCar(brand,size,**parts):
    parts['brand'] = brand
    parts['size'] = size
    return parts

car = makeCar('subaru','B',color='blue',towPackage=True)
print(car)

