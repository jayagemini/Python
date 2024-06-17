"""
Given an integer array arr of size n, find all magic triplets in it.
Magic triplet is a group of three numbers whose sum is zero.
Note that magic triplets may or may not be made of consecutive numbers in arr.
"""

def ThreeSum(inparr):
    inparr.sort()
    resarr=[]
    triplet=[]
    numDict={}

    print ("The input array after sorting :" , inparr)

    for i in range(0,len(inparr)-2):
        l=i+1
        r=len(inparr)-1
        if inparr[i]<=0:
            if i>0 and inparr[i]==inparr[i-1] and inparr[i]!=0:
                continue
            else:
                while l<r:
                    sum=inparr[i]+inparr[l]+inparr[r]
                    if sum>0:
                        r=r-1
                    elif sum<0:
                        l=l+1
                    elif sum==0:
                        triplet=[inparr[i],inparr[l],inparr[r]]
                        resarr.append(triplet)
                        #triplet=str(inparr[i])+", "+str(inparr[l])+", "+str(inparr[r])
                        l=l+1
                        """ if triplet not in numDict:
                            numDict[triplet]=i                        
                            resarr.append(triplet)"""
                
            
    print("Result is :",resarr)       
    return resarr      

test= [-3,4,3,-3,1,2]
print(ThreeSum(test))