#编写函数： 一年 365 天， 每周工作 5 天，休息 2 天，休息日水平下降
#0.01，工作日要努力到什么程度一年后的水平才与每天努力 1%所取得的效果（即
#37.78 倍）一样呢？

def HowEffect(day,degree,n):#计算一年后的效果
    if day==366:
        return degree
    if (day%6==0|day%7==0):
        return HowEffect(day+1,degree*0.99,n)
    else :
        return HowEffect(day+1,degree*(n+1),n)

def funn(n):#计算努力程度
    while(abs(HowEffect(1,1.0,n)-37.78)>0.000000000001):
        if (HowEffect(1,1.0,n)>37.78 ):
            #print(n)
            n=n+pow(HowEffect(1,1.0,n),1/365)-pow(37.78,1/365)
        elif (HowEffect(1,1.0,n)<37.78):
            #print(n)
            n=n+pow(37.78,1/365)-pow(HowEffect(1,1.0,n),1/365)
    return n
print(HowEffect(1,1,funn(0.01)))
print("工作日要努力到",funn(0.01),)