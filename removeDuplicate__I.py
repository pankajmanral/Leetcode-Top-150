nums =  [1,1,2]

class Solution:
    def removeDuplicate_I(self,nums:int) -> int:
        k = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:         
                nums[k] = nums[i-1]
                k+=1
            
        return k
    
sol = Solution()
result = sol.removeDuplicate_I(nums)
print(result)