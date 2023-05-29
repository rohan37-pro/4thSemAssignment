# 1.
# write a python script to print a dictionary where the keys are numbers between 1 and 15 (both included and the values) and the values are the sqare of the keys.
d = {}
for i in range(1,16):
    d[i] = i**2
print(d)
#output - 
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}



# 2.
# write a python program to remove a key from a dictionary
d = {1 : 'one', 2: 'two', 3: 'three'}
d.pop(1) 
del d[3]
print(d)
# output- 
# {2: 'two'}



# 3. 
# write a python progeram to combine two dictionary by adding values for common keys
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a':300, 'b':200, 'd':400}
for i in d1:
    if i in d2:
        d2[i] += d1[i]
    else :
        d2[i] = d1[i]
print(d2)
#output - 
# {'a': 400, 'b': 400, 'd': 400, 'c': 300}



# 4.
# write a program to determine which class a given taxi object belongs to.
class c1 :
    def which_class(self):
        print("object is from class 1")
class c2 :
    def which_class(self):
        print("object is from class 2")
taxi1 = c1()
taxi2 = c2()
taxi1.which_class()
taxi2.which_class()
# output - 
# object is from class 1
# object is from class 2


# 5. 
# creat4e a child class taxi that will inherit all of the variable and methods of the vehicle class
class vehicle :
    wheel = 4
    speed_limit = "80km/h"
    def colour(self, color):
        self.color = color

class taxi(vehicle):
    def __init__(self):
        self.colour('yellow')
    def properties(self):
        print("wheel : ", self.wheel)
        print("speed limit : ", self.speed_limit)
        print("colour : ", self.color)
t1 = taxi()
t1.properties()
#output - 
# wheel :  4
# speed limit :  80km/h
# colour :  yellow