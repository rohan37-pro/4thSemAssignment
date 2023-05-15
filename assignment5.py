# 1.
# wap to sum all the items in a list
def sum_list_elememts():
    data = input("enter numbers : ").strip().split(" ")
    sum = 0
    for i in data:
        sum+=int(i)
    print(sum)


# 2.
def find_largest_num_from_list():
    data = input("enter list of num : ").strip().split(" ")
    greatest = 0
    for i in data:
        if greatest < int(i):
            greatest = int(i)
    print(greatest)
# find_largest_num_from_list()


# 3.
#write a python to count string from a list of strings, where sytring length is 2 or more and last charactgers are teh same
def count_string():
    data = input("enter list of strings : ").strip().split(' ')
    count = 0
    for i in data :
        if len(i) >= 2 and i[0] == i[-1]:
            count += 1
    print(count)
# count_string()


# 4.
#  write a program to display unique and duplicate items of a list
def unique_and_duplicate():
    data = input("enter a list : ").strip().split()
    dic = {}
    for i in data:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    print("unique : ", [i for i in dic if dic[i]==1])
    print("duplicate : ", [i for i in dic if dic[i]!=1])
# unique_and_duplicate()


# 5.
# wap to exchange list half elemets of list with second half element of list 
def exchange_list_elements():
    data = input("enter list : ").strip().split(" ")
    for i in range(-len(data), len(data)//2):
        data[i], data[i + len(data)//2] = data[i + len(data)//2],  data[i]
    print(data)
# exchange_list_elements()

# 6.
# write a program that takes a list 'L' as an argument, adds 5 in all the odd values and 10 in all the even values of the list L also displey the list
def add_5_and_10():
    data = input("enter list : ").strip().split(" ")
    for i in range(len(data)):
        if int(data[i])%2 == 0 :
            data[i] = int(data[i]) + 10
        else :
            data[i] = int(data[i]) + 5
    print(data)


# 7.
# Write a program to display frequencies of an elements of a list
def display_element_frequencies():
    data = input("enter a list : ").strip().split()
    dic = {}
    for i in data:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic:
        print(i, ":", dic[i])
# display_element_frequencies()



# 8. 
# Write a program to display square of an element if it is an integer and change the case if element is a string list is recieved as argument which contains both numbers and strings
def squart_the_list():
    data = input("enter a list : ").strip().split()
    for i in data:
        i = int(i)
        print(i, "=>", i**2)
# squart_the_list()


# 9.
# write a python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both include)




# 10. 