'''
    面向过程：


    面向对象：java ，里程碑的语言
        1996 - 詹姆斯.高斯林，java面向
        python

    车：  车的图纸
        属性(变量)：颜色，轮胎，品牌
        行为（方法）：跑，拉货

    创建一辆车：


'''
#  水杯图纸
class cup:
    color = ""
    height = 0
    volume = 0
    Material = ''

    def run(self):
        print('一个',self.color,'的被子里面放了',self.volume,'ml的水')
# 水杯
c = cup()

c.color = "绿色"
c.height = 5
c.volume = 500
c.Material = '玻璃'

c.run()





























