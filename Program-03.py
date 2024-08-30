#Reverse a word in string 
s= "Abhinav Muarya"
words = s.split()

words =words[::-1]
c = ""
for i in words:
    c += i 
    c += " "

print(c)
