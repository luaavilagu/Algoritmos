//Tomado de: http://www.sanfoundry.com/cpp-program-find-fibonacci-numbers-iteration/

#include <cstring>
#include <iostream>
#include <cstdlib>
#define ll long long
using namespace std;
 
/* 
 * Iterative function to find Fibonacci Numbers 
 */
ll fibo_iter(long long int n)
{
    long long int previous = 1;
    long long int current = 1;
    long long int next = 1;
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
    //int overflow n : 45 
    //long int overflow n : 46
	//long long int overflow n : 134
    
    long long int n = 134;
	    //if (n == 0)
        //    break;
        cout<<fibo_iter(n)<<endl;
    return 0;
}
