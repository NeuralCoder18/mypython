#include <iostream>
#include <cmath>
using namespace std;
// For priting Armstrong Number between 100 and 999
int main(){
    for(int i=100;i<=999;i++){
        int a=i;
        int sum=0;
        while(a>0){
            int last_digit=a%10;
            sum=sum+pow(last_digit,3);
            a=a/10;

        }
        if (sum==i) {
            cout<<i<<endl;
        }
    }

    return 0;
}