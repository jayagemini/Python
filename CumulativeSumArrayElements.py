"""
Write a function that returns the cumulative sum of elements in a 
list
"""
def solution(input):
    output=[]
    Cumsum=0
    for i in range(0, len(input)):
        Cumsum=Cumsum +input[i]
        output.append(Cumsum)

    
    return output





print( solution([1,1,1]))# == [1,2,3]
print( solution([1,-1,3]) )# ==== [1,0,3