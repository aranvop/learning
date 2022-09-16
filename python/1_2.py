#利用 if 判断来制作一个猜数字的小游戏
import random
y=random.randint(0,100)
print("请猜这个数是多少")
x = int (input())#input输入的只能是字符串，所以需要转换为int类型
while 1:
    if x<y:
        print("too small")
    if x>y:
        print("too large")
    if x==y:
        print("right")
        break
    x=int(input("请继续猜"))
