"""
The question says that the integer can be repeated 2 times at most.

Make sure the list is sorted in ascending order otherwise sort the array/list first.
"""

nums = [0,0,1,1,1,1,2,3,3]

class Solution:
    def removeDuplicate_II(self,nums:int) -> int:
        k = 1
        counter = 1     #initially the counter is set to 1

        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:        # if the number appears twice the increment the counter
                counter +=1
            else:
                counter = 1

            if counter <= 2:
                nums[k] = nums[i] 
                k += 1
        return k 
    
sol = Solution()
result = sol.removeDuplicate_II(nums)
print(result)