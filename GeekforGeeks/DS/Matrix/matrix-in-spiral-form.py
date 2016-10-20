def spiralForm(a):


    top = 0
    bottom = len(a) - 1
    left = 0
    right = len(a[0]) - 1

   

    while((top <= bottom) and (left <= right)):
        
        # Top-most row 
        for it in range(left, right + 1):
            print a[top][it],

        top += 1

        # Right-most col
        for it in range(top, bottom + 1):
            print a[it][right],

        right -= 1

        if top <= bottom:

            # Bottom most rows
            for it in range(right, left+1):
                print a[bottom][it],

            bottom -= 1

        if left <= right:

            for it in range(bottom, top+1):
                print a[it][left],

            left += 1


        


        
            

    




a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
spiralForm(a)