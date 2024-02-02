class Solution:
    def generate(self,numRows: int):
        res=[[1]]

        for i in range(numRows-1):
            print("Generate "+str(res))
            print(res[-1])
            temp = [0]+res[-1]+[0]
            print("temp Generate "+str(temp))
            row=[]

            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        return res   

    
s=Solution()
print(s.generate(5))

