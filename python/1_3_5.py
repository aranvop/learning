
def HowEffect(day,degree,n):
    if day==366:
        return degree
    if (day%6==0|day%7==0):
        return HowEffect(day+1,degree*0.99,n)
    else :
        return HowEffect(day+1,degree*(n+1),n)


def nt1(n):
    while(HowEffect(1,1.0,n)!=37.78):
        if (HowEffect(1,1.0,n)>37.78):
            if (HowEffect(1,1.0,n)-37.78>0.1):
                print(n)
                n=n-0.00001#n-pow(HowEffect(1,1.0,n)-37.78,(1/365/7*5))+1
            elif (HowEffect(1,1.0,n)-37.78>0.00001):
                n=n-0.000000001
            else :
                print(n)
                n=n-0.000000000001
        elif (HowEffect(1,1.0,n)<37.78):
                if(37.78-HowEffect(1,1.0,n)>0.1):
                    print(n)
                    n=n+0.00001#pow(37.78-HowEffect(1,1.0,n),(1/365/7*5))-1
                elif(37.78-HowEffect(1,1.0,n)>0.00001):
                    print(n)
                    n=n+0.000000001
                else :
                    print(n)
                    n=n+0.000000000001
    return n

print(HowEffect(1,1,nt1(0)))