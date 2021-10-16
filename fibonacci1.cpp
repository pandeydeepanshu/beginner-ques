#include <bits/stdc++.h>
using namespace std ;

int fib(int n)
{
    if(n<0)
    { 
        cout<<"incorrect value entered";
    }
    else if (n==0 or n==1 )
    {
        return n;
    }
    else 
    return fib(n-1) + fib(n-2);
}
int main ()
{ 
    int n ;
    cout << "please enter a no";
    cin>>n;
    cout << fib(n);
    getchar();
    return 0;
}