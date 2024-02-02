
def ncr(n, r):

    nCrArray=[[1]]
    for i in range(n):
        temp = [0]+nCrArray[-1]+[0]
        row=[]
        for j in range(len(nCrArray[-1]) + 1):
            row.append(temp[j]+temp[j+1])
        nCrArray.append(row)
    #print (nCrArray  )   
    return nCrArray[n][r]


print(ncr(200,100))