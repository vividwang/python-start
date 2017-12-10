import matplotlib.pyplot as plt

xValues = list(range(1,1001))
yValues = [x**2 for x in xValues]

plt.scatter(xValues,yValues,edgecolor='none',s = 40)#edgecolor = 'none'删除黑色轮廓

#设置图表标题，并给坐标轴加上标签
plt.title('Square Number',fontsize = 24)
plt.xlabel('Value',fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)

#设置刻度标记的大小
plt.tick_params(axis='both',labelsize = 14)

#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])
plt.show()