"""
Write a function that returns the elements on odd positions (0 
based) in a list
"""


def solution(input):
    print(1)
    OddList=[]
    print(1)
    for i in range(1, len(input)):
        print(i)
        if i%2!=0:
            OddList.append(input[i])
            print(OddList)
    print(OddList)
    return OddList


test=[1,-1,2,-2]
print(solution(test))




