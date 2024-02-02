
def find_combinations(n, k):
    res= []

    def backtrack(start, comb):
        if len(comb)==k:
            res.append(comb.copy())
            return
            
        for i in range(start, n+1):
            comb.append(i)
            backtrack(i+1,comb)
            comb.pop()

    backtrack(1,[])     
    return res



for i in (find_combinations(6, 4)):
    print(i)
 






















        
        
        
        
        
        
