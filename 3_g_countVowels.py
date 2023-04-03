# WAP TO COUNT THE number of vowels in the pieapple

s = input("enter : ")

vowels = "aeiou"
vow_dict = {}
count = 0
for i in s:
    if i in vowels:
        count+= 1
        if i in vow_dict:
            vow_dict[i] += 1
        else :
            vow_dict[i] = 1

print(f"total vowels count {count} --> ")
for i in vow_dict:
    print(f"vowel {i} : {vow_dict[i]}")