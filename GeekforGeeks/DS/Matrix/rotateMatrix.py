def rotateMatrixBy90AnticlockWise(a):

    r = len(a) - 1
    c = len(a[0]) - 1

    cycles = r/2

    for i in range(cycles):

        for j in range(i, r - i):

            temp = a[i][j]
            a[i][j] = a[j][r-i]
            a[j][r-i] = a[r-i][r-j]
            a[r-i][r-j] = 
