# WAP to print this pattern
# G 
# G A 
# G A N
# G A N G
# G A N G A


s="GANGA"
for i in range(len(s)):
    for j in range(0, i+1):
        print(s[j], end=" ")
    print()