class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 ,len2 = len(str1),len(str2)

        def isDivisor(i):
            if len1%i or len2%i:
                return False
            f1,f2 = len1 //i,len2 //i
            return str1[:i]*f1==str1 and str1[:i]*f2 == str2

        

        for i in range(min(len1,len2),0,-1):
            if isDivisor(i):
                return str1[:i]
        return "" 
    

# Create an instance of the Solution class
solution = Solution()

# Define the input strings
str1 = str(input(("Enter the first string")))
str2 = str(input(("Enter the second string")))
# Call the gcdOfStrings method and print the result
result = solution.gcdOfStrings(str1, str2)
print(result)  # Output should be "ABC"
