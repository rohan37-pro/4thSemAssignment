#  WAP to accept a string and display the word which has vowel 'a' in it

s = input("enter : ")
for i in s.split(" "):
    if 'a' in i.lower():
        print(i)
