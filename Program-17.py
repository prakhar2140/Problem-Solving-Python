class Solution:
    def kidWithExtraCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        result = []

        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result

# Create an instance of the Solution class
solution = Solution()
candies = [1, 2, 4, 3, 5, 6]
extraCandies = 3
# Call the kidWithExtraCandies method and print the result
result = solution.kidWithExtraCandies(candies, extraCandies)
print(result)  # Output: [True, True, True, True, True, True]