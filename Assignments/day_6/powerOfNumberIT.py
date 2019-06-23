# Power of a number using iteration. 


base = float(input("Enter a number:\t\t\t"));
exponentDuplicate = exponent = int(input("Enter the exponent value:\t"));

product = 1;

while (exponent>0) :
    product = product*base;
    exponent = exponent - 1; 
#if (exponent == 0) : product = 1;

while (exponent<0) :
    product = 1/(product*base);
    exponent = exponent + 1;

print ("\n" , base , " to the power " , exponentDuplicate , " is :\t", product , "\n")   