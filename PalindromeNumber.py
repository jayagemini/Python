class Solution(object):
    def isPalindrome(x):
        inputasarray=list(str(x))
       # reversearray=list(reversed(inputasarray))
        reversearray=[]
        for i in range(len(inputasarray)-1, -1,-1):
            reversearray.append(inputasarray[i])


        if inputasarray==reversearray:
            return True
        else:
            return False
        

print(Solution.isPalindrome(121))        

        