
def find_fibonacci(n):

    # Write your code here.
    fibArray=[]
    for i in range(0,n+1):
        if i==0 or i==1:
            fibArray.append(i)
        else:
            fibArray.append(fibArray[i-1]+fibArray[i-2])
        
            
    
    return fibArray[n]


print (find_fibonacci(5))