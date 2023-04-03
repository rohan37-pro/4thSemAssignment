# Write a programme the reads a string and then prints a string that capitalizes every other letter in the string eg - sChOoL

s = input("enter : ")

string = ""
for i in range(len(s)):
    if i%2==0 :
        string += s[i].lower()
    else:
        string += s[i].upper()

print(string)