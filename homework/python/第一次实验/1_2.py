#利用 if 判断来制作一个猜数字的小游戏
import random
def inputNum(str):
    while True:
        try:
            num = int(input(str))
            return num
        except ValueError:
            print("您输入的不是整数，请再次尝试输入！")
#input输入的只能是字符串，所以需要转换为int类型还可能不是数字需要抛出异常
y=random.randint(0,100)
x=inputNum("请猜这个数是多少")
count=10
while (count!=0):
    if x<y:
        print("too small")
    if x>y:
        print("too large")
    if x==y:
        print("right")
        break
    count=count-1
    if (count!=0):
        print("还有",count,"次机会")
        x=inputNum("请继续猜")
    else :
        print("次数用完了，正确答案是：",y)
