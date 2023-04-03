# write a programme to remove vowels from the string

s = input("enter : ")
vowels = "AEIOUaeiou"

vowel_removed = ""
for i in s :
    if i not in vowels:
        vowel_removed += i

print(vowel_removed)