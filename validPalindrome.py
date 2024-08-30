# Total Time Complexity:
# Iteration and Filtering: O(n)
# Joining the List into a String: O(n)
# Reversing the String and Comparison: O(n)

# Since all the operations are linear in time, the overall time complexity of the solution is:

# Total Time Complexity
# =𝑂(𝑛)+𝑂(𝑛)+𝑂(𝑛)=𝑂(𝑛)

# Total Time Complexity= O(n) + O(n) + O(n) = O(n)

s = "A man, a plan, a canal: Panama"

class Solution:
    def validPalindrome(self,s:str) -> bool:

        newString = []      # This a new string to append all the alnum -> alpha numeric characters from the given string

        for char in s:
            if char.isalnum():      # If the char is not alnum() then it doesn't appends it eg : ,space,: etc
                newString.append(char.lower())

        string = ''.join(newString)     # to convert the list(newString) -> string(single word)

        if string == string[::-1]:
            return True
        else:
            return False

sol = Solution()
result = sol.validPalindrome(s)
print(result)




        