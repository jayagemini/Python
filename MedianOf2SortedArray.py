class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A,B=nums1,nums2
        total= len(nums1) +len(nums2)
        half=total//2
        if len(B)<len(A):
            A,B=B,A
        l,r=0, (len(A)-1)
        while True:
            i=(l+r)//2
            j=half-i-2

            ALeft=A[i] if i >=0 else float("-infinity")
            ARight=A[i+1] if (i+1)<len(A) else float("infinity")
            BLeft=B[j] if j >=0 else float("-infinity")
            BRight=B[j+1] if (j+1)<len(B) else float("infinity")

            if ALeft<=BRight and BLeft<=ARight:
                if total%2:
                    return min(ARight, BRight)
                else:
                    return (max(ALeft, BLeft)+min(BRight, ARight))/2
            elif ALeft>BRight:
                r=i-1
            else:
                l=i+1




c=Solution()
print("The median is = ", c.findMedianSortedArrays([1,2],[3,4]))                



        

        
        