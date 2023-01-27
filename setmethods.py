fruits={"apple","banana","orange"}
print(type(fruits))
print(len(fruits))
print(fruits)
fruits.pop()
print(fruits)
fruits.add("mango")
print(fruits)
fruits.clear()
print(fruits)


s1={1,2,3,4}
s2={3,4,5,6}
print(s1.difference(s2))
print(s1.union(s2))
print(s1.intersection(s2))
s1.difference_update(s2)
s1.intersection_update(s2)
print(s1)
