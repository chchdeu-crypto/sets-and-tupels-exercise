#mission 1
tags={"python","bash","git","python"}
print(tags)
print(len(tags))
#mission 2
tags.add("linux")
print(tags)
#mission 3
tags.discard("bash")
print(tags)
tags.discard("c+")
print(tags)
#mission 4
a={1,2,3,}
b={3,4,5,}
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
#mission 5
print("git" in tags)
#mission 6
point=(10,20)
print(point)
print(point[0])
print(point[1])
#mission 7
#point[0]=99
#'tuple' object does not support item assignment
#mission 8
rgb=(255,128,0)
num_1=rgb[0]
num_2=rgb[1]
num_3=rgb[2]
print(num_1)
print(num_2)
print(num_3)
#mission 9
coords=(1,2,3,2,1)
print(coords.count(2))
print(coords.index(1))
print(coords.index(3))
#mission 10
list_1=[1,2,3]
set_1={1,2,3,}
tuple_1=(1,2,3)
print(list_1)
print(set_1)
print(tuple_1)


#part 2
#mission 1
a={1,2,3}
b={3,4,5,}
print(a.issubset(b))
print(a.issuperset(b))
#mission 2
pairs=[(1,"a"),(2,"b"),(3,"c")]
print(pairs[1][1])
#mission 3
my_list=[1,2,3,1,1,]
my_set=set(my_list)
print(my_set)
my_set=list(my_set)
print(my_set)
#mission 4
x={"chaim","yossi"}
y={"avi","mor"}
print(x.symmetric_difference(y))
#mission 5
#Because only primitive values ​​can be inserted into a set and a list is not a primitive value and a tuple is 