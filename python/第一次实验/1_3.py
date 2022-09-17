'''计算斐波那契数列中小于n的所有值'''
def fib_i(a,b,n,count):
    if a >= n:
        print("大于n的数有：",count)
        #return count
    if a < n:
       #return  
       return fib_i(a+b,a,n,count+1)
n=int(input("input n\n"))
#print (fib_i(1,0,n,0))
fib_i(1,0,n,0)