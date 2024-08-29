nums = [2,7,11,15]
target = 9

# First method
# Time complexity => o(n) ^ 2

class Solution():
    def twoSum(self,nums:int,target:int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

# Second method
# Time complexity => o(n)

# This solution only works if the list is sorted in ascending order

# class Solution():
#     def twoSum(self,nums:int,target:int) -> list[int]:
#         nums.sort()
#         start = 0
#         end = len(nums) - 1
#         while start < end:
#             result = nums[start] + nums[end]
#             if result == target:
#                 return [start,end]
#             elif result > target:
#                 end -= 1
#             else:
#                 start += 1

sol = Solution()
result = sol.twoSum(nums,target)
print(result)