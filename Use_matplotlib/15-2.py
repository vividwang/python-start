import matplotlib.pyplot as plt

xValues = list(range(0,5000))
yValues = [x**3 for x in xValues]

plt.scatter(xValues,yValues,c=yValues,cmap=plt.cm.Blues,s=40)

#设置图表标题，并给坐标轴加上标签
plt.title('Square Number',fontsize = 24)
plt.xlabel('Value',fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)

#设置刻度标记的大小
plt.tick_params(axis='both',labelsize = 14)
plt.show()
