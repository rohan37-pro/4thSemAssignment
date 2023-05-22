
# 1 .
# write a python program to create a tuple with different data types.
a = (1, 2.0, 'hello', (1,2,3), [1,2,3], {1: 'a', 2: 'b'})
print(a)


# 2.
# write a python program to convert a tuple to a string
t = (1,2,3)
s = str(t)
print(s)
print(type(s))


# 3.
# write a python program to get the 4th element from the last element of a tuple
a = (1,2,3, 4,5,6,7,8,9,10)
print(a[-4])


# 4.
# write a python program to find repeated items in a tuple
a = eval(input("enter a tuple : "))
for i in a :
    if a.count(i) > 1:
        print(i)


#  5.
# write a python program to check whether an element exists within a tuple.
a = (1,2,4,8,12,16,17,20)
b = int(input("enter number : "))
if b in a :
    print(b, "exists in typle")
else :
    print(b, "not exists")


# 6.
# write a python program to convert a list to a tuple
l = [1,2,3]
print(type(l), l)
print("converting into tuple...")
t = tuple(l)
print(type(t),t)


#  7.
# write a python program to slice a tuple
t = (1,2,3,4,5)
print(t[2:4])



# 8.
# write a program to convert a tuple to a dictionary
t = ("this", 'is', 'a', 'sample', 'text')
d = {}
for i in range(len(t)):
    d[i+1] = t[i]
print(d)



# 9.
# write a python program to reverse a tuple
t = (1,2,3,4,5)
print(t[-1::-1])


# 10.
# write a program to sort a tuple by its float element,
# sample data : [('item1','21.20'), ('item2', '25.30'), ('item3', '34.25')]
a = (21.30, 25.30, 34.25)
b = sorted(a, reverse=True)
print(b)
