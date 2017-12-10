from random import choice

class Randomwalk():
    """一个生成随机漫步数据的类"""
    def __init__(self,num_points = 5000):
        self.num_points = num_points
        #所有随机漫步都始于（0，0）
        self.xValues = [0]
        self.yValues = [0]

    def fillWalk(self):
        """计算随机漫步包含的所有点"""

        #不断漫步，直到列表达到指定长度
        while len(self.xValues) < self.num_points:
            """决定前进方向以及沿这个方向前进的距离"""
            xDirection = choice([1,-1])
            xDistance = choice([0,1,2,3,4])
            xStep = xDirection*xDistance

            yDirection = choice([1, -1])
            yDistance = choice([0, 1, 2, 3, 4])
            yStep = yDirection * yDistance

            #拒绝原地踏步
            if xStep == 0 and yStep == 0 :
                continue

            #计算下一个点的x值和y值
            nextX = self.xValues[-1] + xStep
            nextY = self.yValues[-1] + yStep

            self.xValues.append(nextX)
            self.yValues.append(nextY)

