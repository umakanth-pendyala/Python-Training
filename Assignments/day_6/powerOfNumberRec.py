#To find power of number using recursion.


base = float(input("Enter any number:\t"))
exponentDuplicate = exponent = int(input("Enter exponent:\t\t"));

def FindPower(base, exponent, product = 1) :
    if (exponent > 0) :
        product = product*base;
        exponent = exponent - 1;    
    elif (exponent < 0) :
        product = 1.0/(product * base);
        exponent = exponent + 1;
    if (exponent != 0) : return FindPower(base, exponent, product);
    return product;

print ("\n" , base , " to the power " , exponentDuplicate , " is :\t", FindPower(base, exponent), "\n")