def rev(str1):
    if str1[::-1] ==str1:#使用if语句判断正负是否相同
        print("是回文联")
    else:
        print("不是回文联")
        
str2 = input("请输入一句话：")
output = rev(str2)
print(output)
