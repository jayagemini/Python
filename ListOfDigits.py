"""
Write a function that takes a number and returns a list of its 
digits
"""
def solution(input):
    output=[]
    Number=input
    while Number >0:
        output.append(Number%10)
        Number=Number//10
  
    output.reverse()
    return output



print (solution(123))# == [1,2,3]
print (solution(400))# == [4,0,0]