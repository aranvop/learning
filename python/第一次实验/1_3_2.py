import math
def prime(n):
    alist=[x for x in range(2,n+1)]
    k=0
    for i in range(0,math.floor(math.sqrt(n+1))):
        m=0
        for j in range(2,n+1):
            if j%alist[k]==0 and j!=alist[k]:
                m+=1
                if j in alist:
                    alist.remove(j)
        k+=1
    print("所得的素数为：",alist)
n = int(input("请输入一个大于2的自然数："))
prime(n)
