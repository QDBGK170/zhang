a = 5000
import random
i = random.randint(0, 150)
print(i)
b = 0
for b in  range(0,10):
    num = input('请输入一个数字')
    num = int(num)
    if num == i:
        print("恭喜你，猜中，本次猜的数字为", num)
        a = a + 500
        break
    elif num < i:
         print("小了")
         a = a - 500
    else:
        print("大了")
        a = a - 500
    if a == 0:
        print("你的金币已空，请充值")
            
    else:
        print("你的金币为", a)






