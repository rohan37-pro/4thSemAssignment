s = input("enter :")
new = ""
for i in range(len(s)):
    if i%2==0 :
        new+= s[i].upper()
    else:
        new += s[i].lower()
print(new)