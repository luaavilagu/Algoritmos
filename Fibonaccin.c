#include <stdio.h>

//int fibo(int n);

// user-defined function to check prime number
long long int fibo(long long int n){
	
    long long int previous = 1;
    long long int current = 1;
    long long int next = 1;
    long long int i = 3;
    for (i; i <= n; ++i){
    	
        next = current + previous;
        previous = current;
        current = next;
        
    }
    return next;
}

int main(){
	
	
    //int overflow n : 46 
    //long int overflow n : 48
	//long long int overflow n : 5680
	long long int n = 5680;
	
        printf("%lld", fibo(n) );
        
    return 0;

}


