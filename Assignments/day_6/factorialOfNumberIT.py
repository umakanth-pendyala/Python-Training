# factorial of number using iteration

number = int(input('Enter any number:\t\t'))
product = 1;

for count in range(1,number+1) :
    product = product*count;
print ('factorial of ', number , " is " , product);    