import sys
import math
from contextlib import redirect_stdout

def digit_array(n):
    sum=n
    while n>0:
        sum=sum+n % 10
        n //= 10
    return sum    



def compute_join_point(s_1, s_2):
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    
    while s_1!=s_2:
        s_1=digit_array(s_1)
        print ("The value of S_1=",s_1)
        s_2=digit_array(s_2)
        print ("The value of S_2=",s_2)
            
    return s_1

print("Joint point value =",compute_join_point (471,480))