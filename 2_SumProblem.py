"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.
"""
"""
def TwoSum(inparr,target):
    inparr.sort()
    resarr=[]

    l,r=0,len(inparr)-1
    while l < r:
        cursum=inparr[l]+inparr[r]
        if cursum<target:
            l+=1            
        elif cursum>target:
            r-=1            
        else:
            resarr.append([inparr[l],inparr[r]]) 
            l+=1  
    return resarr
    """

def TwoSum(inparr,target):
    numDict={}
    result=[]
    for i in range(0,len(inparr)):        
        searchVal=target-inparr[i]
        if searchVal in numDict:
            result.append(i)
            result.append(numDict[searchVal])
            print (numDict)
            return result
        print ("Value to be searched =", searchVal)
        print (numDict)
        numDict[inparr[i]]=i
        print (numDict)
        

"""
Time complexity = O(n)
Space complexity = O(n)
"""


test= [1,2,1,3,2,1,3]
target=6
print("Input array is ", test)
print("Target = ", target)
print(TwoSum(test,target))