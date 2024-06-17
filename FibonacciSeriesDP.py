
def find_fibonacci(n):
    result=0
    FibSeries=[0,1]
    for i in range(2,n+1):
        print(i)
        FibSeries.append(FibSeries[i-1]+FibSeries[i-2])  
    
    result=FibSeries[n]
    
    return result


print(find_fibonacci(43))