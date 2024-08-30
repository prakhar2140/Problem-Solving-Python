#WAP to check length of the largest substring without repeating character 
word1= str(input("Enter the string"))
len1=len(word1)

for i in range(0,len1):
    for j in range(i,len1):
        if(word1[i]== word1[j+1]):
            str1 = word1[:i]
        
print(str1)        


