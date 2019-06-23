# factorial of number using recursion
 
number = int(input("enter a number:\t"))

def returnFactorial(num) :
    if (num == 1) : return 1;
    elif (num == 0) : return 0;
    elif (num < 0) : return -1;
    else : return num*returnFactorial(num-1);
print ("factorial of ", number , "is:\t", returnFactorial(number));        