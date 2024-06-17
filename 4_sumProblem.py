"""
Given a list of numbers, 
find all the unique quadruples that sum up to a given target value.
1 <= size of the input list <= 300
-105 <= any element of the input list <= 105
-4 * 105 <= target value <= 4 * 105
"""



def four_sum(arr, target):
    # Write your code here.
    arr.sort()
    numDict={}
    #global res, quad
    quad=[]
    res= []
    
    
    def kSum(k,start, target,quad):  
              
        if k!=2:
            for i in range(start, len(arr)-k+1):
                quad.append(arr[i])
                kSum(k-1,i+1,target-arr[i],quad)
                quad.pop()
            return
        l,r=start, len(arr)-1
        while l<r:
                if arr[l]+arr[r]>target:
                    r=r-1
                elif arr[l]+arr[r]<target:
                    l=l+1
                elif arr[l]+arr[r]==target:
                    res.append(quad+ [arr[l],arr[r]])
                    l=l+1
                    while l<r and arr[l]==arr[l-1]:
                         l=l+1
        
    kSum(4,0,target,quad)                 
    return res


arr=[2, 1, 6, 3, 1, 3, 5, 4, 4, 5, 6, 2]
targt=11
print(four_sum(arr, targt))