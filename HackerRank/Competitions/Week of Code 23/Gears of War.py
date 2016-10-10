"""
Input Format:

The first line contains single integer, , denoting the number of queries. 
Each line  of the  subsequent lines contains a single integer, n, denoting the number of gears for that query.

Output Format:

For each query, print Yes on a new line if it is possible to rotate all n gears simultaneously; otherwise, print No.
"""

def gearsOfWar():

    q = int(raw_input())

    for i in range(q):
        n = int(raw_input())
        if n % 2 == 0:
            print "Yes"

        else:
            print "No"

gearsOfWar()
