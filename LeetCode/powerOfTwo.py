class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
            
        oneBitCount = 0
        for i in range(32):
            if ( (n & 1) == 1):
                oneBitCount += 1
                
            n = n >> 1
        return oneBitCount == 1