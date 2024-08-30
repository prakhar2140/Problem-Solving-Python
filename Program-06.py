word1 = str(input("Enter the string"))
len1 = len(word1)
if(len1<2):
    word1.reset()
    print(word1)
else:
    str1=word1[0:2]
    str2=word1[-2:]
    str3 =str1+str2 
    print(str3)
