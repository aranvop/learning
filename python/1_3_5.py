
def HowEffect(day,degree,n):
    if day==366:
        return degree
    if (day%6==0|day%7==0):
        return HowEffect(day+1,degree*0.99,n)
    else :
        return HowEffect(day+1,degree*(n+1),n)

def funn(n):
    while(abs(HowEffect(1,1.0,n)-37.78)>0.000000000001):
        if (HowEffect(1,1.0,n)>37.78 ):
            #print(n)
            n=n+pow(HowEffect(1,1.0,n),1/365)-pow(37.78,1/365)
        elif (HowEffect(1,1.0,n)<37.78):
            #print(n)
            n=n+pow(37.78,1/365)-pow(HowEffect(1,1.0,n),1/365)
    return n
print(HowEffect(1,1,funn(0)))