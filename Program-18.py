class Solution:
    def compress(self,chars:list[str])-> int:
        n=  len(chars)
        list1 = []
        list1 = set(chars)
        chars = list(list1)
        for i in range(n):
            if (len(chars)==1):
                return chars
            elif(chars.count(i)>1):
                a = chars.count(i)
                a.append(list1)
        return(list1)
        







#Create a instance for the Solution class 
solution = Solution()

chars = ["a","a","b","b","c","c","c"]
#Call the compress function and print  the result 
result = solution.compress(chars)
print(result)
       