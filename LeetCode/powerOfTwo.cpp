class Solution {
public:
    bool isPowerOfTwo(int n) {
        
        if(n <= 0){
            return false;
        
    }
    
    int oneBitCount = 0;
    for(int i = 0; i < 32; i++){
        if(n & 1 == 1){
            oneBitCount++;
        }
        
    n = n >> 1;
    
    }
    
    return oneBitCount == 1;
    }
};