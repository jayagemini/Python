def n_choose_k(n,k):
    if n==k or k==0:
        return 1
    else:
        return int((n/k)*n_choose_k(n-1,k-1))
    


def n_choose_k1(n,k):
    if n==k or k==0:
        return 1
    else:
        return n_choose_k1(n-1,k) + n_choose_k1(n-1,k-1)
    


print (n_choose_k(5,4))    

print (n_choose_k1(5,4))  
    

