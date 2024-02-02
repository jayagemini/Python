def ConvertNumberto64Base(n):
    digit=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','-','_']
    numberrep=[]
    currvalue=n
    print('The input number is ',n)
    while currvalue>64:
        remainder=currvalue%64
        currvalue=currvalue//64
        
        print ('Quotient=', str(currvalue))
        print ('remainder=', remainder)
        numberrep.append(digit[remainder])

    if currvalue>0:
        numberrep.append(digit[currvalue]) 
    print (numberrep    )
    numberrep.reverse()
    tinyURl=''.join(map(str, numberrep))
    return tinyURl

    




print('http://bit.ly/'+ConvertNumberto64Base(3478595))
