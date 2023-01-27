str1=str(input("Enter the string:"))
list1=list(str1)
list2=[]
for x in list1:
    if x!="A" and x!="E " and x!="I" and x!="O" and x!="U":
        list2.append(x)
        str2=" "join(list2)
        print(str2)
    else:
        print(-1)
