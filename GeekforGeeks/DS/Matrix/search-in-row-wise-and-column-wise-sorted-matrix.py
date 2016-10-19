def search(a, element):

    rows = len(a)
    columns = len(a[0])

    i = 0
    j = columns - 1

    while( i < rows and j >= 0):
        if a[i][j] == element:
            print 'found at', i, j
            return 

        if a[i][j] > element:
            j -= 1

        else:
            i += 1

    print 'not found'






a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
search(a, 5)