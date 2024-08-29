# In this question we have to merge the two list *in-place* i.e we cannot use extra space the 0's in the nums1 list 
# The 0's have to be replaced 

nums1 = [1,2,3,0,0,0] 
nums2 = [2,5,6]
m = 3
n = 3

class Solution():
    def merge(self,nums1:int,num2:int,m:int,n:int) -> None:
        p1 = m - 1      #position of the last number in nums1
        p2 = n - 1      #position of the last number in nums2
        index = len(nums1) - 1      #index of where the bigger number should be placed in the nums1 list 

        while p1 >= 0 and p2 >= 0:
            n1 = nums1[p1]
            n2 = nums2[p2]

            if n1 > n2:
                nums1[index] = n1
                p1 -= 1
            else:
                nums1[index] = n2
                p2 -= 1
            index -= 1

        while p2 >= 0:
            nums1[index] = nums2[p2]
            p2 -= 1
            index -= 1

sol = Solution()
result = sol.merge(nums1,nums2,m,n)
print(nums1)