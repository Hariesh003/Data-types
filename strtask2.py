str1=str(input("enter the string:"))
list1=list(str1)
list2=[]
for x in list1:
    if list1.count(x)>=1:
       list2.append(x)
str2=" ".join(x)
print(str2)
