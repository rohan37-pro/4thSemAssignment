# WAP to accept a stering and display the string with csecond alphabet and each in lowercase

s = input("enter :")
new = ""
for i in range(len(s)):
    if i%2==0 :
        new+= s[i].upper()
    else:
        new += s[i].lower()
print(new)