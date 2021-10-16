def fib(n):#defining a function
    #if value smaller than 0 is entered it will return false in output
    if n<0 :
        return False
    #if n is  0 or 1 it will return the same value
    elif n==0 :
        return n
    elif n==1 :
        return n
    #the main function 
    #it can tell value upto n= 25 but after that the pc takes time to execute the code as the 
    #value become very high can take a lot of processing time
    else :
        return fib(n-1)+fib(n-2)
#print statement
print(fib(-2))