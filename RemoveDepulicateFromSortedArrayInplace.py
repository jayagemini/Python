class Solution(object):
    def removeDuplicates(self, nums):

        
        l=1
        r=1
        while r< len(nums) and l<len(nums):
            if nums[r]==nums[r-1]:
                r=r+1
            else:                
                nums[l]=nums[r]
                l=l+1
                r=r+1
                

        return l            

        
        
        return nums


input=[0,0,1,1,1,2,2,3,3,4]   
c=Solution()
print("=================================================")
print(c.removeDuplicates(input))
        