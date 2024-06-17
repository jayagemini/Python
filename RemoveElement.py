class Solution(object):
    def removeElement(self, nums, val):
        F=0
        for i in range (len(nums)):
            if nums[i]!=val:
                nums[F]=nums[i]
                K+=1
                               

        return F        




        
        
input=[3,3]  
k=3
"""input=[0,1,2,2,3,0,4,2]  
k=2""" 
c=Solution()
print("=================================================")
print(c.removeElement(input,k))
                