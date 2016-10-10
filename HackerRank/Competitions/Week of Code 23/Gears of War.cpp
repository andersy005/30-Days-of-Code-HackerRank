#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void gearsOfWar(){
    int q;
    int n;
    cin >> q;
    
    for(int i = 0; i < q; q++){
       cin >> n;
        if (n % 2 == 0){
            cout <<"Yes"<<endl;
        }
        
         else if (n % 2 != 0) {
            cout <<"No"<<endl;
        }
    }
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    gearsOfWar();
    return 0;
}
