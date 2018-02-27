//Tomado de: http://www.sanfoundry.com/cpp-program-find-fibonacci-numbers-iteration/

#include <cstring>
#include <iostream>
#include <cstdlib>
#define ll long long
using namespace std;
 
/* 
 * Iterative function to find Fibonacci Numbers 
 */
ll fibo_iter(int n)
{
    int previous = 1;
    int current = 1;
    int next = 1;
    for (int i = 3; i <= n; ++i) 
    {
        next = current + previous;
        previous = current;
        current = next;
    }
    return next;
}
/* 
 * Main
 */
int main()
{
    //int overflow n : 2140000000 
    //long int overflow n : 1999999999
	//long long int overflow n : 9150000000000000000
    
    int n = 2140000000;
	    //if (n == 0)
        //    break;
        cout<<fibo_iter(n)<<endl;
    return 0;
}
