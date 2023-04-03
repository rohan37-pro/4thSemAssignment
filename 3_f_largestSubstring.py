# WAP that reads a string and displays the longest substring of the given string.

s = input("enter :")

greatest = 0
for i in s.strip().split(" "):
    if len(i) > greatest:
        greatest = len(i)

print(f"longest string of size {greatest} --> ")
for i in s.strip().split(" "):
    if len(i) == greatest :
        print(i)