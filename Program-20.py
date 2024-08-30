#WAP to convert the integer to Roman number 
class Solution:
    def intToRoman(self, num: int) -> str:
        dict1 = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,
        "L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1
        } 
        result = ""  
        for key, value in dict1.items():
            while num >= value:
                result += key
                num -= value 
        return result

solution = Solution()
num = 3749
result = solution.intToRoman(num)                                    
print(result)
