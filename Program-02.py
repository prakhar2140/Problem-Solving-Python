#Wap to reverse the vowels of the string in python
vowels = ['a','e','i','o','u','A','E','I','O','U']
word1 = str(input("Enter the string:-"))

i=0
j=len(word1)-1
c=0
while(i<j):
    if word1[i] not in vowels:
        i += 1
    elif word1[j] not in vowels:
        j += 1
    else:
        c=word1[i]
        word1[i]= word1[j]
        word1[j] = c
        i+=1

'''class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        i=0
        j=len(s)-1
        while(i<j):
            if s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i+=1
                j-=1
        return ''.join(s)'''