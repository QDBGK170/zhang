class Computer :
    screen = 0
    Price = 0
    cpu = ''
    memory = ''
    time = 0

    def typing(self):
        print('使用电脑在打字')
    def game(self,gamename):
        print('在打',gamename)
    def Video(self,vid):
        print('使用电脑在看',vid,'总决赛')

c = Computer()
c.screen = 15.6
c.price = 5000
c.cpu = 'i9 11900k'
c.memory = '1TB'
c.time = 24

c.game('彩六：围攻')
c.Video('major')