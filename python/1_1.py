import random
y=random.randint(0,100)
print("请猜这个数是多少")
x = int (input())#input输入的只能是字符串，所以需要转换为int类型
if x<y:
    print("too small")
if x>y:
    print("too large")
if x==y:
    print("right")