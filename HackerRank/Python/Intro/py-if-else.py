#!/bin/python3

import sys


N = int(input().strip())

# If N is odd
if N % 2 != 0:
    print("Weird")
    
# else if N is even

else:
    
    if N in range(2,6):
        print("Not Weird")
        
    elif N in range(6, 21):
        print("Weird")
        
    else:
        print("Not Weird")