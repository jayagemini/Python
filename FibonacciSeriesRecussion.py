
def find_fibonacci(n):
    result=0
    
    if n==1:
        return 1
    
    if n==0:
        return 0
    
    result=find_fibonacci(n-2) + find_fibonacci(n-1)  
    
    
    
    return result


print(find_fibonacci(43))