# 

s = input("enter : ")

vowels = "aeiou"
vow_dict = {}
for i in s:
    if i in vowels:
        if i in vow_dict:
            vow_dict[i] += 1
        else :
            vow_dict[i] = 0

print("vowels count in string --> ")
for i in vow_dict:
    print(f"vowel {i} : {vow_dict[i]}")