def modifyMatrix(a):

    rows = len(a) - 1
    cols = len(a[0]) - 1


    rowFlag = False
    colFlag = False

    # Scan the first row and set rowFlag to indicate whether we need to set all 1s in the first row or not

    for i in range(cols + 1):
        if a[0][i] == 1:
            rowFlag = True
            break
       

    
    # Scan the first col and set colFlag

    for i in range(rows + 1):
        if a[i][0] == 1:
            colFlag = True
            break 
        

    """Use first row and first column as the auxiliary arrays row[] and col[] respectively, 
    consider the matrix as submatrix starting from 
    econd row and second column and apply method 1"""
    for i in range(1, rows + 1):

        for j in range(1, cols + 1):

            if a[i][j]:

                a[i][0] = 1
                a[0][j] = 1


    # Finally, using rowFlag and colFlag, update first row and first column if needed
    for i in range(1, rows+1):

        for  j in range(1, cols+1):

            if a[i][0]  or a[0][j]:
                a[i][j] = 1


    if rowFlag:
        for i in range(rows+1):
            a[i][0]=1

    if colFlag:
        for i in range(cols+1):
            a[0][i]=1

    return a 


a = [[0,0,0],
     [0,0,1]]
print(modifyMatrix(a))

    