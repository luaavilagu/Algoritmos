#include <stdio.h>

//int fibo(int n);

// user-defined function to check prime number
int fibo(unsigned long int n){
	
    unsigned long int previous = 1;
    unsigned long int current = 1;
    unsigned long int next = 1;
    unsigned long int i = 3;
    for (i; i <= n; ++i){
    	
        next = current + previous;
        previous = current;
        current = next;
        
    }
    return next;
}

int main(){
	
	
    //int overflow n : 2140000000 
    //long int overflow n : 1999999999
	//long long int overflow n : 2140000000000000000
	//unsigned long long int n : 9090000000000000000
	//unsigned long int n : 4240000000;
	unsigned long int n = 4240000000;

        printf("%d", fibo(n) );
        
    return 0;

}


