# WAP that reads a line, then count words and display how many words are there in the line.

s = input("enter : ")

s_list = s.strip().split(" ")
print("word count --> ", len(s_list))
