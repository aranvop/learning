import random
y=random.randint(0,100)
print("请猜这个数是多少")
while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是整数，请再次尝试输入！")
#input输入的只能是字符串，所以需要转换为int类型还可能不是数字需要抛出异常
if x<y:
    print("too small")
    print("true number is :" ,y)
elif x>y:
    print("too large")
    print("true number is :" ,y)
else :
    print("right")
